import os
from dotenv import load_dotenv

load_dotenv(os.getenv("ENV_FILE", ".env"))

class Config:
    INDEX_NAME = os.getenv("INDEX_NAME")