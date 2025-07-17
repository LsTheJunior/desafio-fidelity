"""
Repositório de acesso a dados para pesquisas jurídicas.

Responsável por encapsular as operações de leitura, escrita e filtragem de dados na tabela 'pesquisas' do TinyDB.
"""

from tinydb import Query
from app.db.database import db


class PesquisaRepository:
    def __init__(self):
        self.table = db.table("pesquisas")

    def get_all(self, skip=0, limit=10):
        return self.table.all()[skip : skip + limit]

    def get_by_filtro(self, filtro):
        PesquisaQ = Query()
        return self.table.search((PesquisaQ.tipo == str(filtro)))

    def insert_many(self, pesquisas):
        self.table.insert_multiple(pesquisas)

    def clear(self):
        self.table.truncate()
