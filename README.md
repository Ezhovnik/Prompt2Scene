# Prompt2Scene: Генерация Manim-анимации по текстовому описанию

Этот репозиторий содержит доработанную (fine-tuned) версию **[Qwen2.5-Coder-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-3B-Instruct)**, которая преобразует текстовые описания в исполняемый код **Manim**.  
Модель дообучена на наборе данных `english_data12.csv`, который был создан путём объединения двух открытых источников (один с [Hugging Face](https://huggingface.co/datasets/shekhar98/manim_community_and_documentation_code), другой с [Kaggle](https://www.kaggle.com/datasets/ravidussilva/manim-sft/data)) и дополнен вручную дополнительными примерами.

## 👥 Команда проекта

Этот проект был выполнен в рамках **проектной деятельности** в **Школе № 179 г. Москвы**.

**Авторы:**
- **[Георгий Харитонов](https://github.com/Ezhovnik)**, 10Д класс
- **[Анна Васильева](https://github.com/179Ann)**, 10Д класс

## 📁 Структура репозитория
```
├── README.md # Этот файл
├── Notebook.ipynb # Jupyter-блокнот
├── english_data12.csv # Обучающие данные (пары «запрос → код»)
└── tune_model_english_qwen_coder.zip # Готовая доработанная модель (распакуйте для использования)
```

---

# Prompt2Scene: Generate Manim Animations from Natural Language

This repository contains a fine-tuned version of **[Qwen2.5-Coder-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-3B-Instruct)** that converts textual descriptions into executable **Manim** code.  
The model is fine-tuned on `english_data12.csv`, a dataset constructed by merging two public sources (one from [Hugging Face](https://huggingface.co/datasets/shekhar98/manim_community_and_documentation_code), one from [Kaggle](https://www.kaggle.com/datasets/ravidussilva/manim-sft/data)) and manually extending with additional examples.

## 👥 Project Team

This project was developed as part of a **project-based learning activity** at **Moscow School No. 179**.

**Authors:**
- **[Georgy Kharitonov](https://github.com/Ezhovnik)**, 10D grade
- **[Anna Vasilyeva](https://github.com/179Ann)**, 10D grade

## 📁 Repository Structure
```
├── README.md # This file
├── Notebook.ipynb # Jupyter notebook
├── english_data12.csv # Training data (prompt → code pairs)
└── tune_model_english_qwen_coder.zip # Fine-tuned model (unzip to use)
```
