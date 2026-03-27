from fastapi import FastAPI

from app.models.series import SeriesRegister


app = FastAPI(
    title = "Catalago de Séries",
    description = "Catalago",
    version = "1.0.0"
)

@app.get ("/")
def home():
    return {"messagem": "Catalago de Séries em construção"}

@app.post("/series/")
def series():
    return SeriesRegister
