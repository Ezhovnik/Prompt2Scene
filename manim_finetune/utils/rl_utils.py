from manim_finetune.utils import eval_utils
from manim_finetune.utils import gemini_utils
from manim_finetune.utils import manim_test_utils
from manim_finetune.constants import GEMINI_MODEL

def generate_candidates(prompt, model, tokenizer, num_candidates, temperature):
    candidates = []
    for _ in range(num_candidates):
        code = eval_utils.run_inference(model, tokenizer, prompt, temperature)
        candidates.append(code)
    return candidates

def test_and_score_candidates(prompt, candidates, gemini_client):
    scored = []
    for code in candidates:
        if manim_test_utils.manim_test(code):
            score = gemini_utils.evaluate_code_with_gemini(
                gemini_client,
                prompt,
                code,
                GEMINI_MODEL
            )
            scored.append((code, score))
    return scored

def select_dpo_pair(prompt, scored_candidates):
    if len(scored_candidates) < 2:
        return None

    codes, scores = zip(*scored_candidates)

    best_idx = scores.index(max(scores))
    worst_idx = scores.index(min(scores))

    if scores[best_idx] > scores[worst_idx]:
        return {
            "prompt": prompt,
            "chosen": codes[best_idx],
            "rejected": codes[worst_idx],
            "chosen_score": scores[best_idx],
            "rejected_score": scores[worst_idx]
        }
    return None

def process_step(prompt: str, model, tokenizer, gemini_client, num_candidates: int, temperature: float):
    candidates = generate_candidates(
        prompt,
        model,
        tokenizer,
        num_candidates,
        temperature
    )
    scored = test_and_score_candidates(
        prompt,
        candidates,
        gemini_client
    )
    return select_dpo_pair(prompt, scored)
