from fastapi import FastAPI

from app.models.series import SeriesRegister

from typing import List



series_catalog: List[dict] = []


app = FastAPI(
    title = "Catalago de Séries",
    description = "Catalago",
    version = "1.0.0"
)

@app.get ("/")
def home():
    return {"messagem": "Catalago de Séries em construção"}

@app.post("/series/")
def create_series(serie: SeriesRegister):
    if serie.ano_lancamento >= 1900 and serie.season >0 :
        series_catalog.append(serie.model_dump())
        return {
            "messagem": "Serie criada com sucesso! ",
            "dados": serie.model_dump()
    }
    else:
        return {"messagem": "Erro ao tentar criar"}


    
