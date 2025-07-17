"""
Módulo de configuração e inicialização do banco de dados TinyDB.

Fornece a instância singleton do banco de dados utilizada em toda a aplicação.
"""

from tinydb import TinyDB

db = TinyDB("db.json")
