"""
Schemas Pydantic para requisições e respostas relacionadas a pesquisas e automação.

Inclui modelos para pesquisa e para requisição de filtro de automação.
"""

from pydantic import BaseModel


class PesquisaSchema(BaseModel):
    cod_pesquisa: str
    nome: str
    cpf: str
    rg: str
    tipo: str
    uf: str


class FiltroRequest(BaseModel):
    filtro: int = 0
