"""
Módulo principal da aplicação FastAPI.

Este módulo inicializa a aplicação, registra os roteadores de pesquisa e automação,
e expõe a interface HTTP para consumo dos endpoints.
"""

from fastapi import FastAPI
from app.routers.pesquisa_router import router as pesquisa_router
from app.routers.automacao_router import router as automacao_router

app = FastAPI()

app.include_router(pesquisa_router)
app.include_router(automacao_router)
