# Prompt2Scene: Генерация Manim-анимации по текстовому описанию

Этот репозиторий содержит доработанную (fine-tuned) версию **[Qwen2.5-Coder-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-3B-Instruct)**, которая преобразует текстовые описания в исполняемый код **Manim**.  
Модель дообучена на наборе данных, который был создан путём объединения двух наборов из открытых источников (один с [Hugging Face](https://huggingface.co/datasets/shekhar98/manim_community_and_documentation_code), другой с [Kaggle](https://www.kaggle.com/datasets/ravidussilva/manim-sft/data)) и дополнен вручную дополнительными примерами.

## 👥 Команда проекта

Этот проект был выполнен в рамках **проектной деятельности** в **Школе № 179 г. Москвы**.

**Авторы:**

- **[Георгий Харитонов](https://github.com/Ezhovnik)**, 10Д класс
- **[Анна Васильева](https://github.com/179Ann)**, 10Д класс

## 📁 Структура репозитория

```plaintext
├── README.md # Этот файл
├── manim.ipynb # Jupyter-блокнот с основной логикой дообучения
├── manim_launch.ipynb # Jupyter-блокнот, в котором можно протестировать manim-код
├── .gitignore
└── manim_finetune
    ├── __init__.py
    ├── constants.py # Основные константы: названия файлов, значения переменных, имя модели и т.д.
    └── utils
        ├── __init__.py
        ├── archive_utils.py # Функции для работы с архивами
        ├── data_utils.py # Функции для обработки данных
        ├── eval_utils.py # Функции для оценки модели
        ├── manim_test.py # Файл с функцией, тестирующей manim-код на наличие RE
        ├── manim_utils.py # Функции для удобной работы с manim
        ├── model_utils.py # Функции, помогающие при дообучении
        ├── gemini_utils.py # Функции, помогающие при работе с Gemini
        └── rl_utils.py # Функции для обучения с подкреплением
```

---

# Prompt2Scene: Generate Manim Animations from Natural Language

This repository contains a fine-tuned version of **[Qwen2.5-Coder-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-3B-Instruct)** that converts textual descriptions into executable **Manim** code.  
The model is fine-tuned on a dataset that was created by combining two datasets from open sources (one from [Hugging Face](https://huggingface.co/datasets/shekhar98/manim_community_and_documentation_code), one from [Kaggle](https://www.kaggle.com/datasets/ravidussilva/manim-sft/data)) and manually extending with additional examples.

## 👥 Project Team

This project was developed as part of a **project-based learning activity** at **Moscow School No. 179**.

**Authors:**

- **[Georgy Kharitonov](https://github.com/Ezhovnik)**, 10D grade
- **[Anna Vasilyeva](https://github.com/179Ann)**, 10D grade

## 📁 Repository Structure

```plaintext
├── README.md # This file
├── manim.ipynb # Jupyter notebook with basic fine-tuning logic
├── manim_launch.ipynb # A Jupyter notebook where you can test manim code
├── .gitignore
└── manim_finetune
    ├── __init__.py
    ├── constants.py # Basic constants: file names, variable values, model name, etc.
    └── utils
        ├── __init__.py
        ├── archive_utils.py # Functions for working with archives
        ├── data_utils.py # Functions for data processing
        ├── eval_utils.py # Functions for evaluating the model
        ├── manim_test.py # A file with a function that tests the manim code for RE
        ├── manim_utils.py # Functions for convenient operation with manim
        ├── model_utils.py # Functions that help with fine tuning
        ├── gemini_utils.py # Functions that help when working with Gemini
        └── rl_utils.py # Functions for reinforcement learning
```
