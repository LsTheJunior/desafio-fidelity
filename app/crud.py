"""
Módulo CRUD para operações com pesquisas no banco TinyDB.

Fornece funções para consulta paginada e logging detalhado das operações realizadas.
"""

from app.database import db
import logging

logger = logging.getLogger(__name__)


def get_pesquisas(skip: int = 0, limit: int = 10):
    logger.info(f"[CRUD] get_pesquisas chamado com skip={skip}, limit={limit}")
    pesquisas = db.table("pesquisas").all()
    logger.debug(f"[CRUD] Conteúdo completo das pesquisas: {pesquisas}")
    result = pesquisas[skip : skip + limit]
    logger.info(
        f"[CRUD] get_pesquisas retornou {len(result)} registros: {[p.get('cod_pesquisa') if isinstance(p, dict) else str(p) for p in result]}"
    )
    return result
