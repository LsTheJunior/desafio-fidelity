"""
Roteador FastAPI para endpoints de pesquisas jurídicas.

Define rotas para listagem paginada de pesquisas, utilizando o serviço de pesquisas e tratamento de exceções.
"""

from fastapi import APIRouter, HTTPException, Query
from app.services.pesquisa_service import PesquisaService
from app.schemas.pesquisa_schema import PesquisaSchema
from typing import List

router = APIRouter(prefix="/pesquisas", tags=["pesquisas"])


@router.get("/", response_model=List[PesquisaSchema])
def listar(skip: int = Query(0, ge=0), limit: int = Query(10, le=100)):
    """Lista pesquisas com paginação."""
    try:
        return PesquisaService().listar_pesquisas(skip, limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
