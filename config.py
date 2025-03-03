import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    assert OPENAI_API_KEY, "OPENAI_API_KEY is not set"
    OPENAI_API_MODEL = os.getenv("OPENAI_API_MODEL")
    assert OPENAI_API_MODEL, "OPENAI_API_MODEL is not set"
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    assert GEMINI_API_KEY, "GEMINI_API_KEY is not set"
    GEMINI_MODEL = os.getenv("GEMINI_MODEL")
    assert GEMINI_MODEL, "GEMINI_MODEL is not set"
    SERPI_API_KEY = os.getenv("SERPI_API_KEY")
    assert SERPI_API_KEY, "SERPI_API_KEY is not set"
    HF_TOKEN = os.getenv("HF_TOKEN")
    assert HF_TOKEN, "HF_TOKEN is not set"

config = Config()

if __name__ == "__main__":
    print(config.OPENAI_API_KEY)
    print(config.OPENAI_API_MODEL)
    print(config.GEMINI_API_KEY)
    print(config.GEMINI_MODEL)
