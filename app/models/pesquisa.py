# Modelos de domínio (opcional, TinyDB é flexível)
class Pesquisa:
    def __init__(self, cod_pesquisa, nome, cpf, rg, tipo, uf):
        self.cod_pesquisa = cod_pesquisa
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.tipo = tipo
        self.uf = uf
