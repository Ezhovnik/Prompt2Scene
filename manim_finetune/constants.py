# Download data
DATASET_ID = "1gb8S-8xharo5YYTOczAB_6YdOiQR_YCj"
TUNE_MODEL_ID = "1TgsqiUSQ6k_Wuw0LR2On1r5j765DeHgZ"

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

# Paths
OUTPUT_DIR = "./results"
SAVE_MODEL_PATH = "./tune_model_english_qwen_coder"
ZIP_NAME = "tune_model_english_qwen_coder"
