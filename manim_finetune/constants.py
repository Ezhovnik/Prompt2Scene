# Download data
DATASET_DRIVE_ID = "1gb8S-8xharo5YYTOczAB_6YdOiQR_YCj"
TUNE_MODEL_DRIVE_ID = "1TgsqiUSQ6k_Wuw0LR2On1r5j765DeHgZ"
DPO_DATASET_DRIVE_ID = "1QfRb-1mLdppG1zOpNpzgSiue3jV3xl22"
DPO_MODEL_DRIVE_ID = ""

# Model
MODEL_NAME = "Qwen/Qwen2.5-Coder-3B-Instruct"

# LoRA params
LORA_R = 6
LORA_ALPHA = 12
DPO_LORA_R = 6
DPO_LORA_ALPHA = 12

# Training
EPOCHS = 7
BATCH_SIZE = 1
GRAD_ACCUM_STEPS = 8
LEARNING_RATE = 2e-4
MAX_LENGTH = 1024
DPO_EPOCHS = 5
DPO_BATCH_SIZE = 1
DPO_GRAD_ACCUM_STEPS = 8
DPO_LEARNING_RATE = 5e-5
DPO_BETA = 0.3
DPO_MAX_LENGTH = 2048

# Dataset
TEST_SIZE = 0.2

# Inference
TEMPERATURE = 0.8
REPETITION_PENALTY = 1.2
MAX_NEW_TOKENS = 500

# Gemini
GEMINI_MODEL = "gemma-4-26b-a4b-it"

# Paths
OUTPUT_DIR = "./results"
DPO_OUTPUT_DIR = "./dpo_results"
SAVE_MODEL_PATH = "./tune_model_english_qwen_coder"
DPO_SAVE_MODEL_PATH = "./dpo_model_english_qwen_coder"
ZIP_NAME = "tune_model_english_qwen_coder"
DPO_ZIP_NAME = "dpo_model_english_qwen_coder"

SYSTEM_MSG = "Write ONLY the code (without text explanations and comments) using the manim library for Python, which corresponds to the user's request."
