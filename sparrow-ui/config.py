import os

class Settings():
    sparrow_key = "01234567890"
    huggingface_key: str = os.environ.get("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")

settings = Settings()