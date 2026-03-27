from pydantic import BaseModel

class SeriesRegister(BaseModel):
    id_: int
    titulo: str
    genero: str
    ano_lancamento: int
    season: int