import os
from dotenv import load_dotenv


load_dotenv()


POKEAPI_URL = os.getenv("POKEAPI_URL")
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT"))
REDIS_TIME_EXPIRED = os.getenv("REDIS_TIME_EXPIRED")
REDIS_USERNAME = os.getenv("REDIS_USERNAME")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")