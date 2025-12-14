import os

def get_env(key: str, default: str) -> str:
    return os.getenv(key, default)

PORT = int(get_env("PORT", "5000"))
DB_URL = get_env("DB_URL", "sqlite:///./runs.db")
MODEL_ID = get_env("MODEL_ID", "qwen2.5-vl-7b-instruct")
