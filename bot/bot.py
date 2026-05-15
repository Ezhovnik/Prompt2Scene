import torch
from peft import PeftModel
from transformers import AutoTokenizer, AutoModelForCausalLM
from manim_finetune import constants as mf_constants
from manim_finetune.utils import archive_utils
from manim_finetune.utils import data_utils
from manim_finetune.utils import eval_utils
from manim_finetune.utils import manim_test_utils
from manim_finetune.utils import manim_utils
import os
import telebot

token = open('token.txt', 'r').readline()
bot = telebot.TeleBot(token)

os.environ["PYTHONUTF8"] = "1"

def get_model():
    if not os.path.exists(mf_constants.SAVE_MODEL_PATH):
        tune_model_filename = mf_constants.ZIP_NAME + ".zip"
        data_utils.download_data(mf_constants.TUNE_MODEL_DRIVE_ID, tune_model_filename)
        archive_utils.extract_zip(tune_model_filename, mf_constants.SAVE_MODEL_PATH)

    adapter_path = mf_constants.SAVE_MODEL_PATH
    base_model_path = os.path.abspath("./base_model")

    tokenizer = AutoTokenizer.from_pretrained(base_model_path, trust_remote_code=True)
    base_model = AutoModelForCausalLM.from_pretrained(
        base_model_path,
        trust_remote_code=True,
        torch_dtype=torch.float16
    )

    model = PeftModel.from_pretrained(base_model, adapter_path)
    model.eval()

    answer = eval_utils.run_inference(model, tokenizer, "Нарисуй круг")
    # print(answer)
    video = manim_utils.manim_render(answer, output_dir="./ab", quality="h")
    # print(video)
    # print(manim_test_utils.manim_test(answer))
    return tokenizer, model

tokenizer, model = get_model()

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        "👋 Здравствуйте! Я бот для создания анимаций Manim.\n\n"
        "Просто напишите текстовое описание того, что хотите увидеть (например: «Нарисуй красный квадрат, который вращается»), "
        "и я попробую сгенерировать код и отрендерить видео.\n\n"
        "⏳ Обработка может занять некоторое время, придется подождать."
    )

@bot.message_handler(content_types=['text'])
def generate(message):
    # print(message.text)
    bot.send_message(message.from_user.id, "Обрабатываю запрос, это может занять время...")
    answer = eval_utils.run_inference(model, tokenizer, message.text)
    answerget = False
    for i in range(10):
        r = manim_test_utils.manim_test(answer)
        # print(r)
        if r:
            answerget = True
            break
        else:
            bot.send_message(message.from_user.id, "Обрабатываю...")
            answer = eval_utils.run_inference(model, tokenizer, message.text)
    if answerget:
        bot.send_message(message.from_user.id, "Верный код:")
        bot.send_message(message.from_user.id, "```python\n" + answer + "\n```", parse_mode='MarkdownV2')
        video = manim_utils.manim_render(answer, output_dir="./temp_dir", quality="h")
        video_file = open(video[1], 'rb')
        bot.send_video(message.chat.id, video=video_file)
        # print(video)

    else:
        bot.send_message(
            message.from_user.id,
            "Простите, запрос оказалось сложнее, чем мы рассчитывали. Попробуйте в другой раз."
        )
    # print(answer)

bot.infinity_polling()
