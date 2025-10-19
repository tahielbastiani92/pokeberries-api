import os
from dotenv import load_dotenv


load_dotenv()


POKEAPI_URL = os.getenv("POKEAPI_URL", "https://pokeapi.co/api/v2/berry")
