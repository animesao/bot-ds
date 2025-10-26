# 🎉 Discord Bot

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![discord.py](https://img.shields.io/badge/discord.py-2.0+-blue.svg)](https://discordpy.readthedocs.io/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4+-blue.svg)](https://www.sqlalchemy.org/)

A comprehensive Discord bot with moderation, welcomes, and leveling systems built with Python, discord.py, and SQLAlchemy.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage Examples](#usage-examples)
- [Recommendations for Improvement](#recommendations-for-improvement)
- [Русская версия](#русскоязычная-версия)

## ✨ Features

- **🛡️ Moderation System**: Commands like `!warn`, `!ban`, `!kick`, `!mute`. Auto-moderation for banned words and spam detection.
- **👋 Custom Welcomes**: Set welcome channel and message with variables like `{user}`, `{server}`.
- **📈 Leveling System**: Gain XP from messages, check rank with `!rank`, view top 10 with `!top10`.
- **🗄️ Database**: SQLite with SQLAlchemy ORM for storing settings, users, warnings, etc.
- **⚙️ Config**: JSON config for defaults, logging setup.
- **📝 Logging**: Actions logged to file for monitoring.

## 🚀 Installation

1. Clone or download the project.
2. Navigate to the `discord_bot` directory.
3. Create virtual environment: `python -m venv venv`
4. Activate venv: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/Mac)
5. Install dependencies: `pip install -r requirements.txt`
6. Edit `.env` and add your Discord bot token: `DISCORD_TOKEN=your_token_here`
7. Run the bot: `python main.py`

## ⚙️ Configuration

- `config.json`: Default settings, logging config.
- `.env`: Discord token.

## 💡 Usage Examples

- **Moderation**: `!warn @user reason`, `!ban @user reason`, `!kick @user reason`, `!mute @user 1h`
- **Welcomes**: `!set_welcome_channel #general`, `!set_welcome_message Welcome {user} to {server}!`
- **Leveling**: `!rank`, `!top10`

## 🔧 Recommendations for Improvement

- Implement full spam detection with message history tracking.
- Add role-based permissions for commands.
- Enhance mute with time-based unmute.
- Add more customization options.
- Use async database operations for better performance.
- Add error handling and user feedback.

---

# 🇷🇺 Русскоязычная версия

## 🎉 Discord Бот

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![discord.py](https://img.shields.io/badge/discord.py-2.0+-blue.svg)](https://discordpy.readthedocs.io/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4+-blue.svg)](https://www.sqlalchemy.org/)

Комплексный Discord бот с системами модерации, приветствий и уровней, построенный на Python, discord.py и SQLAlchemy.

## 📋 Содержание

- [Функции](#функции)
- [Установка](#установка)
- [Конфигурация](#конфигурация)
- [Примеры использования](#примеры-использования)
- [Рекомендации по улучшению](#рекомендации-по-улучшению)

## ✨ Функции

- **🛡️ Система модерации**: Команды типа `!warn`, `!ban`, `!kick`, `!mute`. Автомодерация для запрещенных слов и обнаружения спама.
- **👋 Кастомные приветствия**: Установка канала приветствий и сообщения с переменными типа `{user}`, `{server}`.
- **📈 Система уровней**: Получение опыта за сообщения, проверка ранга с `!rank`, просмотр топ-10 с `!top10`.
- **🗄️ База данных**: SQLite с ORM SQLAlchemy для хранения настроек, пользователей, предупреждений и т.д.
- **⚙️ Конфиг**: JSON конфиг для дефолтных настроек, логирования.
- **📝 Логирование**: Действия логируются в файл для мониторинга.

## 🚀 Установка

1. Клонируйте или скачайте проект.
2. Перейдите в директорию `discord_bot`.
3. Создайте виртуальное окружение: `python -m venv venv`
4. Активируйте venv: `venv\Scripts\activate` (Windows) или `source venv/bin/activate` (Linux/Mac)
5. Установите зависимости: `pip install -r requirements.txt`
6. Отредактируйте `.env` и добавьте токен бота Discord: `DISCORD_TOKEN=your_token_here`
7. Запустите бота: `python main.py`

## ⚙️ Конфигурация

- `config.json`: Дефолтные настройки, конфиг логирования.
- `.env`: Токен Discord.

## 💡 Примеры использования

- **Модерация**: `!warn @user причина`, `!ban @user причина`, `!kick @user причина`, `!mute @user 1h`
- **Приветствия**: `!set_welcome_channel #general`, `!set_welcome_message Добро пожаловать {user} на {server}!`
- **Уровни**: `!rank`, `!top10`

## 🔧 Рекомендации по улучшению

- Реализовать полное обнаружение спама с отслеживанием истории сообщений.
- Добавить ролевые разрешения для команд.
- Улучшить мут с временным размутом.
- Добавить больше опций кастомизации.
- Использовать асинхронные операции базы данных для лучшей производительности.
- Добавить обработку ошибок и обратную связь пользователям.
