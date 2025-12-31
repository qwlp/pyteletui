import os
from dotenv import load_dotenv
from telegram.client import Telegram

load_dotenv()

def envOrThrow(var):
    if os.getenv(var) is not None:
        return os.getenv(var)
    else:
        raise KeyError(f"env {var} not found")

def client() -> Telegram:
    tg = Telegram(
        api_id=envOrThrow('API_ID'),
        api_hash=envOrThrow('API_HASH'),
        phone=envOrThrow('PHONE'),
        database_encryption_key=envOrThrow('DB_ENCRYPTION_KEY'),
    )

    get_chats_result = tg.get_chats()
    get_chats_result.wait()

    tg.login()
    return tg
