from fastapi import APIRouter, HTTPException
from app.models.series import SeriesRegister
from typing import List
import json
import sqlite3

router = APIRouter()

@router.post("/")
def create_series(serie: SeriesRegister):
    try:
        # Tenta abrir o arquivo. Se não existir, cria uma lista vazia
        try:
            with open("series.json", "r") as file:
                series = json.load(file)
        except FileNotFoundError:
            series = []

        # Adiciona a nova série
        series.append(serie.model_dump())

        # Salva tudo de volta no arquivo
        with open("series.json", "w") as file:
            json.dump(series, file, indent=4)

        return {
            "mensagem": "Série criada com sucesso!",
            "serie": serie.model_dump()
        }
    except Exception as e:
        # Erro inesperado no processo
        raise HTTPException(
            status_code=500,
            detail=f"Erro interno ao criar a série: {str(e)}"
        )



@router.get("/")
def listar_series():
    try:
        with open ("series.json", "r") as file:
            series = json.load(file)
            return series
    except FileNotFoundError: 
        return []


@router.get("/series/{titulo}")
def buscar_series(titulo: str):
    conexao = sqlite3.connect('series.db')
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT titulo, genero, ano_lancamento, temporadas
        FROM series
        WHERE LOWER (titulo) = LOWER(?)''', (titulo,))
    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        return{
            "titulo": resultado[0],
            "genero": resultado[1],
            "ano_lancamento": resultado[2],
            "temporadas": resultado[3]
        }
    else:
        raise HTTPException(
            status_code=404,
            detail="Serie não encontrada"
        )
