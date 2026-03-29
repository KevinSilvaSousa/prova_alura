from pydantic import BaseModel, field_validator


class SeriesRegister(BaseModel):
    titulo: str 
    genero: str
    ano_lancamento: int 
    temporadas: int

    @field_validator("ano_lancamento")
    def validar_ano_lancamento(cls, ano_lancamento): 
            if ano_lancamento < 1900:
                raise ValueError ("Ano de lancamento invalido")
            return ano_lancamento
    

    @field_validator("temporadas")
    def validar_temporadas(cls, temporadas):
        if temporadas < 1:
            raise ValueError("Temporadas invalidas")
        return temporadas 
    
    @field_validator("titulo")
    def validar_titulo(cls, titulo):
        if titulo is None:
            raise ValueError("titulo invalido")
        return titulo
    

    @field_validator("genero")
    def validar_genero(cls, genero):
        if genero is None:
            raise ValueError("genero invalido")
        return genero
             

