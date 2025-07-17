"""
Roteador FastAPI para endpoints de automação de pesquisas.

Define rotas para execução de automações por filtro ou para todos os filtros, utilizando tarefas em background e tratamento de exceções.
"""

from fastapi import APIRouter, HTTPException, BackgroundTasks
from app.schemas.pesquisa_schema import FiltroRequest
from app.services.automacao_service import AutomacaoService
from app.core.logger import logger

router = APIRouter(prefix="/automacao", tags=["automacao"])


def run_automacao(filtro):
    AutomacaoService(filtro).executar()
    logger.info(f"Automação finalizada para filtro={filtro}")


@router.post("/executa-filtro")
def executa_filtro(body: FiltroRequest, background_tasks: BackgroundTasks):
    try:
        background_tasks.add_task(run_automacao, body.filtro)
        return {"status": "Automação agendada", "filtro": body.filtro}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/executa-todos")
def executa_todos(background_tasks: BackgroundTasks):
    try:
        for filtro in range(4):
            background_tasks.add_task(run_automacao, filtro)
        return {"status": "Automação agendada para todos os filtros"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
