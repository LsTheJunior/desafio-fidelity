import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from app.repositories.pesquisa_repository import PesquisaRepository
from tinydb import TinyDB

# Garante que a tabela 'pesquisas' existe mesmo se o arquivo não existir
TinyDB(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../db.json"))).table(
    "pesquisas"
)

if __name__ == "__main__":
    print("Populando tabela 'pesquisas'...")
    repo = PesquisaRepository()
    repo.clear()
    repo.insert_many(
        [
            {
                "cod_pesquisa": "1",
                "nome": "João Teste",
                "cpf": "12345678900",
                "rg": "1234567",
                "tipo": "0",
                "uf": "SP",
            },
            {
                "cod_pesquisa": "2",
                "nome": "Maria Teste",
                "cpf": "98765432100",
                "rg": "7654321",
                "tipo": "0",
                "uf": "SP",
            },
            {
                "cod_pesquisa": "3",
                "nome": "Carlos Nome",
                "cpf": "",
                "rg": "",
                "tipo": "0",
                "uf": "SP",
            },
        ]
    )
    print("Tabela 'pesquisas' populada com sucesso!")
    sys.exit(0)
