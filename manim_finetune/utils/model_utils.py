import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import LoraConfig, get_peft_model, TaskType
from trl import SFTTrainer, SFTConfig, DataCollatorForCompletionOnlyLM

def load_model_and_tokenizer(model_name: str, bnb_config: BitsAndBytesConfig = None):
    """Load model"""

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=bnb_config,
        device_map="auto",
        low_cpu_mem_usage=True
    )
    return tokenizer, model

def apply_lora(model, r: int = 6, alpha: int = 12, target_modules = None):
    """Wrap model with LoRA adapters."""
    peft_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=r,
        lora_alpha=alpha,
        target_modules = target_modules
    )
    return get_peft_model(model, peft_config)

def create_data_collator(tokenizer, response_template: str = "<|im_start|>assistant\n"):
    """Create data collator for completion-only LM."""
    return DataCollatorForCompletionOnlyLM(
        response_template=response_template,
        tokenizer=tokenizer,
    )

def create_trainer(model, tokenizer, train_dataset, eval_dataset, training_args):
    """Create SFTTrainer instance."""
    data_collator = create_data_collator(tokenizer)
    trainer = SFTTrainer(
        model=model,
        data_collator=data_collator,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
    )
    return trainer

def save_model(trainer, save_path: str):
    """Save trained model."""
    trainer.save_model(save_path)
