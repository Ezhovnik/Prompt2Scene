# Download data
DATASET_DRIVE_ID = "1gb8S-8xharo5YYTOczAB_6YdOiQR_YCj"
TUNE_MODEL_DRIVE_ID = "1TgsqiUSQ6k_Wuw0LR2On1r5j765DeHgZ"
DPO_DATASET_DRIVE_ID = "1QfRb-1mLdppG1zOpNpzgSiue3jV3xl22"

# Model
MODEL_NAME = "Qwen/Qwen2.5-Coder-3B-Instruct"

# LoRA params
LORA_R = 6
LORA_ALPHA = 12

# Training
EPOCHS = 7
BATCH_SIZE = 1
GRAD_ACCUM_STEPS = 8
LEARNING_RATE = 2e-4
MAX_LENGTH = 1024
EVAL_STEPS = 50
LOGGING_STEPS = 50
SAVE_STEPS = 250
SAVE_TOTAL_LIMIT = 5

# Dataset
TEST_SIZE = 0.2

# Inference
TEMPERATURE = 0.8
REPETITION_PENALTY = 1.2
MAX_NEW_TOKENS = 500

# Gemini
GEMINI_MODEL = "gemma-3-27b-it"

# Paths
OUTPUT_DIR = "./results"
SAVE_MODEL_PATH = "./tune_model_english_qwen_coder"
ZIP_NAME = "tune_model_english_qwen_coder"
