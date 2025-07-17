"""
Serviço de regras de negócio para pesquisas jurídicas.

Responsável por intermediar as operações entre os repositórios de dados e os roteadores,
fornecendo métodos para listagem e filtragem de pesquisas, além de registrar logs das operações.
"""

from app.repositories.pesquisa_repository import PesquisaRepository
from app.core.logger import logger


class PesquisaService:
    def __init__(self):
        self.repo = PesquisaRepository()

    def listar_pesquisas(self, skip=0, limit=10):
        logger.info(f"Listando pesquisas: skip={skip}, limit={limit}")
        return self.repo.get_all(skip, limit)

    def listar_por_filtro(self, filtro):
        logger.info(f"Listando pesquisas por filtro: {filtro}")
        return self.repo.get_by_filtro(filtro)
