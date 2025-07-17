-- Script de criação das tabelas no PostgreSQL
CREATE TABLE estado (
    cod_uf VARCHAR PRIMARY KEY,
    uf VARCHAR,
    cod_fornecedor VARCHAR,
    nome VARCHAR
);

CREATE TABLE lote (
    cod_lote VARCHAR PRIMARY KEY,
    cod_lote_prazo VARCHAR,
    data_criacao DATE,
    cod_funcionario VARCHAR,
    tipo VARCHAR,
    prioridade VARCHAR
);

CREATE TABLE lote_pesquisa (
    cod_lote_pesquisa VARCHAR PRIMARY KEY,
    cod_lote VARCHAR REFERENCES lote(cod_lote),
    cod_pesquisa VARCHAR REFERENCES pesquisa(cod_pesquisa),
    cod_funcionario VARCHAR,
    cod_funcionario_conclusao VARCHAR,
    cod_fornecedor VARCHAR,
    data_entrada DATE,
    data_conclusao DATE,
    cod_uf VARCHAR REFERENCES estado(cod_uf),
    obs TEXT
);

CREATE TABLE pesquisa_spv (
    cod_pesquisa VARCHAR PRIMARY KEY,
    cod_spv VARCHAR,
    cod_spv_computador VARCHAR,
    cod_spv_tipo VARCHAR,
    cod_funcionario VARCHAR,
    filtro TEXT,
    website_id VARCHAR,
    resultado TEXT
);

CREATE TABLE servico (
    cod_servico VARCHAR PRIMARY KEY,
    civel BOOLEAN,
    criminal BOOLEAN
);

CREATE TABLE pesquisa (
    cod_pesquisa VARCHAR PRIMARY KEY,
    cod_cliente VARCHAR,
    cod_uf VARCHAR REFERENCES estado(cod_uf),
    cod_servico VARCHAR REFERENCES servico(cod_servico),
    tipo VARCHAR,
    cpf VARCHAR,
    cod_uf_nascimento VARCHAR,
    cod_uf_rg VARCHAR,
    data_entrada DATE,
    data_conclusao DATE,
    nome VARCHAR,
    nome_corrigido VARCHAR,
    rg VARCHAR,
    rg_corrigido VARCHAR,
    nascimento DATE,
    mae VARCHAR,
    mae_corrigido VARCHAR,
    anexo TEXT
);
