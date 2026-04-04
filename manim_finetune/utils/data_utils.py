import pandas as pd
import gdown
from datasets import Dataset

def download_data(file_id: str, output_name: str):
    """Download CSV from Google Drive."""
    url = f"https://drive.google.com/uc?id={file_id}&confirm=t"
    gdown.download(url, output_name, quiet=False)

def load_data(csv_path: str) -> pd.DataFrame:
    """Load CSV into DataFrame."""
    return pd.read_csv(csv_path)

def format_instruction(sample: dict) -> dict:
    """Format a single sample into the chat template string."""
    text = (
        "<|im_start|>system\n"
        "Write ONLY the code (without text explanations and comments) using the manim library for Python, which corresponds to the user's request."
        "<|im_end|>\n"
        "<|im_start|>user\n"
        f"{sample['prompt']}"
        "<|im_end|>\n"
        "<|im_start|>assistant\n"
        f"{sample['response']}"
        "<|im_end|>"
    )
    return {"text": text}

def create_datasets(df: pd.DataFrame, tokenizer, test_size: float = 0.2, max_length: int = 1024, seed: int = 42):
    """
    Convert DataFrame to Dataset, split into train/test, filter long examples.
    Returns train_dataset, test_dataset.
    """
    dataset = Dataset.from_pandas(df[["prompt", "response"]])
    dataset = dataset.map(format_instruction, remove_columns=["prompt", "response"])

    # Split
    split = dataset.train_test_split(test_size=test_size, seed=seed)
    train_dataset = split["train"]
    test_dataset = split["test"]

    # Filter test examples with at least 2 tokens
    def min_tokens(example):
        tokens = tokenizer.encode(example['text'])
        return len(tokens) >= 2
    test_dataset = test_dataset.filter(min_tokens)

    # Filter test examples where assistant response is present after truncation
    def filter_long(example):
        tokens = tokenizer(example["text"], truncation=True, max_length=max_length)
        decoded = tokenizer.decode(tokens["input_ids"])
        return "<|im_start|>assistant\n" in decoded
    train_dataset = train_dataset.filter(filter_long)
    test_dataset = test_dataset.filter(filter_long)

    return train_dataset, test_dataset

def edit_row(df: pd.DataFrame, index: int, new_prompt: str, new_response: str) -> pd.DataFrame:
    """
    Edit a specific row in the DataFrame.
    Returns modified DataFrame (in-place modification).
    """
    df.loc[index] = [new_prompt, new_response]
    return df

def add_row(df: pd.DataFrame, prompt: str, response: str) -> pd.DataFrame:
    """
    Append a new row to the DataFrame.
    Returns modified DataFrame (in-place modification).
    """
    new_row = pd.DataFrame({"prompt": [prompt], "response": [response]})
    return pd.concat([df, new_row], ignore_index=True)

def save_dataset(df: pd.DataFrame, csv_path: str) -> None:
    """Save DataFrame to CSV."""
    df.to_csv(csv_path, index=False)
