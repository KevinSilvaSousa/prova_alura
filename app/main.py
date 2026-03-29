# Bibliotecas Python
from fastapi import FastAPI


# Imports do codigo
from app.routers.series import router


app = FastAPI(
    title = "Catalago de Séries",
    description = "Catalago",
    version = "1.0.0"
)
# Aqui ficará as rotas
app.include_router(router, prefix="/series", tags=["Series"])
app.include_router(router,prefix="/series/listas", tags=["Listar"])
app.include_router(router, prefix="/series/buscar", tags=["Buscar"])

@app.get ("/")
def home():
    return {"mensagem": "Catalago de Séries em construção"}
