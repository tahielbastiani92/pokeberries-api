from fastapi import FastAPI


app = FastAPI(title="Pokeberries API")


@app.get("/")
def intial():
    return {"message": "Working.. Pokeberries statistics is coming.."}