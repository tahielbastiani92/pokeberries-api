from fastapi import FastAPI


app = FastAPI(title="Pokerberries API")


@app.get("/")
def intial():
    return {"message": "Working.. Pokeberries statistics is coming.."}