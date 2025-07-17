from tinydb import TinyDB

db = TinyDB('db.json')
pesquisas = db.table('pesquisas')
pesquisas.truncate()  # Limpa a tabela
pesquisas.insert_multiple([
    {
        "cod_pesquisa": "1",
        "nome": "João Teste",
        "cpf": "12345678900",
        "rg": "1234567",
        "tipo": "0",
        "uf": "SP"
    },
    {
        "cod_pesquisa": "2",
        "nome": "Maria Teste",
        "cpf": "98765432100",
        "rg": "7654321",
        "tipo": "0",
        "uf": "SP"
    }
])
print("Tabela 'pesquisas' populada com sucesso!")
