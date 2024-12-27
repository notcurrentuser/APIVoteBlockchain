# Перша ініціалізація

## Встановлення пакетів
Для Windows та venv

`pip install -r .\requirements.txt`

Для Linux

`pip3 install -r requirements.txt`

## Ініціалізація бази даних
Для Windows та venv

`python init_db.py`

Для Linux

`python3 init_db.py`

# Запуск проекта

## Запуск API сервера

`uvicorn web.base:app --reload`
