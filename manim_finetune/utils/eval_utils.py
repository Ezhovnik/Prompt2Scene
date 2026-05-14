# manim_finetune/eval_utils.py
import torch
import pandas as pd
from manim_finetune.utils import manim_test_utils
import constants

def run_inference(model, tokenizer, prompt: str, temperature: float = 0.8, max_new_tokens: int = 500, repetition_penalty: float = 1.2) -> str:
    """Generate code from a prompt using the model."""
    messages = [
        {"role": "system", "content": constants.SYSTEM_MSG},
        {"role": "user", "content": prompt}
    ]
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        temperature=temperature,
        repetition_penalty=repetition_penalty,
        max_new_tokens=max_new_tokens,
    )
    generated_tokens = outputs[0][inputs['input_ids'].shape[1]:]
    code = tokenizer.decode(generated_tokens, skip_special_tokens=True)

    clean_code = code
    start_index = code.find("```python")
    if start_index != -1:
        start = start_index + len("```python")
        end = code.find("```", start)
        if end != -1:
            clean_code = code[start:end].strip()
    return clean_code

def evaluate_model(model, tokenizer, df: pd.DataFrame, n_samples: int = 100, temperature: float = 0.8, max_new_tokens: int = 500, repetition_penalty: float = 1.2, log_file: str = "manim_errors.log", seed: int = 42):
    """
    Randomly sample n_samples from df, run inference, test code with manim.
    Returns (accuracy, list_of_failed_indices).
    """
    random_samples = df.sample(n=n_samples, random_state=seed)
    failed = []
    for idx, row in random_samples.iterrows():
        torch.cuda.empty_cache()
        code = run_inference(model, tokenizer, row['prompt'], temperature, max_new_tokens, repetition_penalty)
        if not manim_test_utils.manim_test(code, log_file, idx):
            failed.append(idx)
    accuracy = (n_samples - len(failed)) / n_samples
    return accuracy, failed
