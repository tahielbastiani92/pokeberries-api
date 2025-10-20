from fastapi import FastAPI
from src.api.routes import router


app = FastAPI(title="Pokeberries API")
app.include_router(router)