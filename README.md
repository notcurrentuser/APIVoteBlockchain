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

`uvicorn web.base:app --port 8762 --reload`

Порт може бути довільним.

# Використання
Для початку потрібно відредагувати config.py файл та перевірити чи є підключення до моста блокчейн мережі.

## Записування даних через API та синхронізація їх з блокчейн

POST `http://ip:port/api/vote` [`http://127.0.0.1:8762/api/vote`]

Запит

`{
    "voter_id": "31946",
    "candidate_id": "1"
}`

Відповідь

`
{
    "voter_id": "31946",
    "candidate_id": "1",
    "timestamp": "2024-12-28T21:52:25.772808",
    "blockchain_tx_hash": "0x1ca34c71ca68852aa5cf336b1b0bb018af919969f02a960695c0bd6861eb3ebe"
}
`

## Отримання даних через API та ID даних в мережі блокчейн

GET `http://ip:port/api/votes` [`http://127.0.0.1:8762/api/votes`]

Відповідь
`
[
    {
        "voter_id": "311646",
        "candidate_id": "1",
        "timestamp": "2024-12-28T21:19:30.795705",
        "blockchain_tx_hash": "0x0ee4bc93b5e7a023eaa613780743ff14ab9a8a1c9ef2bc0cb8e735170fd26953"
    },
    {
        "voter_id": "3112246",
        "candidate_id": "1",
        "timestamp": "2024-12-28T21:12:30.292104",
        "blockchain_tx_hash": "0xb7feb89ded54689ffa4facc032802a8518a2c87ee3acfb9ffc74efc2ff20a9cb"
    },
    {
        "voter_id": "31003106",
        "candidate_id": "2",
        "timestamp": "2024-12-28T21:09:07.699102",
        "blockchain_tx_hash": "0x7c0666b46db75b44a2019a5a3cb11db8c0cd888f905de9a2b1e04a7a42d38b2e"
    },
]
`
