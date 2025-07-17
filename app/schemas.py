"""
Schemas Pydantic para validação e serialização de dados de pesquisas.

Define modelos base e de saída para pesquisas, utilizados em endpoints e serviços.
"""

from pydantic import BaseModel
from typing import Optional, List
from datetime import date


class PesquisaBase(BaseModel):
    cod_pesquisa: str
    cod_cliente: Optional[str]
    cod_uf: Optional[str]
    cod_servico: Optional[str]
    tipo: Optional[str]
    cpf: Optional[str]
    cod_uf_nascimento: Optional[str]
    cod_uf_rg: Optional[str]
    data_entrada: Optional[date]
    data_conclusao: Optional[date]
    nome: Optional[str]
    nome_corrigido: Optional[str]
    rg: Optional[str]
    rg_corrigido: Optional[str]
    nascimento: Optional[date]
    mae: Optional[str]
    mae_corrigido: Optional[str]
    anexo: Optional[str]


class PesquisaOut(PesquisaBase):
    pass
