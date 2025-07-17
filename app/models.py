from sqlalchemy import Column, String, Date, Boolean, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Estado(Base):
    __tablename__ = "estado"
    cod_uf = Column(String, primary_key=True)
    uf = Column(String)
    cod_fornecedor = Column(String)
    nome = Column(String)


class Servico(Base):
    __tablename__ = "servico"
    cod_servico = Column(String, primary_key=True)
    civel = Column(Boolean)
    criminal = Column(Boolean)


class Pesquisa(Base):
    __tablename__ = "pesquisa"
    cod_pesquisa = Column(String, primary_key=True)
    cod_cliente = Column(String)
    cod_uf = Column(String, ForeignKey("estado.cod_uf"))
    cod_servico = Column(String, ForeignKey("servico.cod_servico"))
    tipo = Column(String)
    cpf = Column(String)
    cod_uf_nascimento = Column(String)
    cod_uf_rg = Column(String)
    data_entrada = Column(Date)
    data_conclusao = Column(Date)
    nome = Column(String)
    nome_corrigido = Column(String)
    rg = Column(String)
    rg_corrigido = Column(String)
    nascimento = Column(Date)
    mae = Column(String)
    mae_corrigido = Column(String)
    anexo = Column(Text)


class Lote(Base):
    __tablename__ = "lote"
    cod_lote = Column(String, primary_key=True)
    cod_lote_prazo = Column(String)
    data_criacao = Column(Date)
    cod_funcionario = Column(String)
    tipo = Column(String)
    prioridade = Column(String)


class LotePesquisa(Base):
    __tablename__ = "lote_pesquisa"
    cod_lote_pesquisa = Column(String, primary_key=True)
    cod_lote = Column(String, ForeignKey("lote.cod_lote"))
    cod_pesquisa = Column(String, ForeignKey("pesquisa.cod_pesquisa"))
    cod_funcionario = Column(String)
    cod_funcionario_conclusao = Column(String)
    cod_fornecedor = Column(String)
    data_entrada = Column(Date)
    data_conclusao = Column(Date)
    cod_uf = Column(String, ForeignKey("estado.cod_uf"))
    obs = Column(Text)


class PesquisaSPV(Base):
    __tablename__ = "pesquisa_spv"
    cod_pesquisa = Column(String, primary_key=True)
    cod_spv = Column(String)
    cod_spv_computador = Column(String)
    cod_spv_tipo = Column(String)
    cod_funcionario = Column(String)
    filtro = Column(Text)
    website_id = Column(String)
    resultado = Column(Text)
