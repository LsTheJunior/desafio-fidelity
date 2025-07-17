# Desafio Fidelity

## Visão Geral
Este projeto automatiza consultas de pesquisas jurídicas em plataformas de tribunais do Brasil, conforme solicitado no desafio técnico da Fidelity Pesquisas Cadastrais. O sistema foi modernizado para seguir boas práticas de desenvolvimento, facilitar manutenção e permitir integração via API REST.

## Principais Tecnologias
- **FastAPI** — API web moderna e rápida
- **TinyDB** — Banco de dados NoSQL leve, baseado em arquivo JSON
- **Selenium** — Automação de consultas web
- **pytest** — Testes automatizados
- **Black** — Formatação automática de código (PEP 8)

## Estrutura do Projeto
```
├── app/
│   ├── main.py                # Inicialização da API FastAPI
│   ├── automation.py          # Lógica de automação Selenium
│   ├── crud.py                # Funções CRUD com TinyDB
│   ├── database.py            # Instância do TinyDB
│   ├── core/                  # Configurações e logger
│   ├── db/                    # Scripts e utilitários de banco
│   ├── models/                # Modelos de domínio
│   ├── repositories/          # Repositórios de acesso a dados
│   ├── routers/               # Rotas da API
│   ├── schemas/               # Schemas Pydantic
│   ├── services/              # Camada de serviços (regras de negócio)
│   └── requirements.txt       # Dependências Python
├── db.json                    # Banco de dados TinyDB
├── tests/                     # Testes automatizados (pytest)
├── README.md                  # Este arquivo
```

## Como Executar o Projeto

### Pré-requisitos
- Python 3.10 ou superior instalado

### Passo a Passo
1. Clone o repositório:
   ```powershell
   git clone https://github.com/LsTheJunior/desafio-fidelity.git
   cd desafio-fidelity
   ```
2. Instale as dependências:
   ```powershell
   pip install -r app/requirements.txt
   ```
3. (Opcional) Popule o banco TinyDB com dados de exemplo:
   ```powershell
   python app/db/popula_db.py
   ```
4. Inicie a API:
   ```powershell
   uvicorn app.main:app --reload
   ```
5. Acesse a documentação interativa em [http://localhost:8000/docs](http://localhost:8000/docs)

## Execução Opcional com Docker

Se preferir, você pode executar o projeto em um ambiente isolado usando Docker. Isso garante que todas as dependências e configurações estejam corretas, independentemente do seu sistema operacional.

### Vantagens de usar Docker
- **Ambiente padronizado:** O projeto roda igual em qualquer máquina (Windows, Linux, Mac), evitando problemas de "na minha máquina funciona".
- **Isolamento:** Não interfere nas dependências de outros projetos Python do seu computador.
- **Fácil de rodar:** Basta um comando para subir tudo pronto para uso.
- **Descarte rápido:** Para remover tudo, basta parar e excluir o container.

### Como executar com Docker
1. Certifique-se de ter o [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado e rodando.
2. Na raiz do projeto, execute:
   ```powershell
   docker build -t desafio-fidelity .
   docker run -it -p 8000:8000 desafio-fidelity
   ```
3. Acesse a API normalmente em [http://localhost:8000/docs](http://localhost:8000/docs)

> **Nunca usou Docker?**
> Veja o guia oficial: [Primeiros passos com Docker](https://docs.docker.com/get-started/)

## Exemplos de uso dos endpoints

### Listar pesquisas (paginação)
```bash
curl -X GET "http://localhost:8000/pesquisas?skip=0&limit=10" -H "accept: application/json"
```

### Executar automação para um filtro
```bash
curl -X POST "http://localhost:8000/automacao/executa-filtro" \
     -H "accept: application/json" \
     -H "Content-Type: application/json" \
     -d '{"filtro": 0}'
```

### Executar automação para todos os filtros
```bash
curl -X POST "http://localhost:8000/automacao/executa-todos" -H "accept: application/json"
```

## Qualidade de Código e Testes

- O projeto utiliza o [Black](https://black.readthedocs.io/) para formatação automática e padronização do código Python (PEP 8). Recomenda-se rodar `black .` na raiz do projeto para garantir o padrão.
- Possui testes unitários automatizados (pytest) localizados na pasta `tests/`, cobrindo as principais regras de negócio e automação.

### Executando os testes

```powershell
pytest tests/
```

## Boas Práticas e Arquitetura

Este projeto foi estruturado seguindo princípios de arquitetura limpa e boas práticas de Python, visando facilitar a manutenção, testes e evolução do sistema. Veja alguns pontos importantes:

- **Divisão em camadas**: O código está organizado em camadas bem definidas:
  - `routers/`: define os endpoints HTTP (interface da API)
  - `services/`: contém as regras de negócio e orquestração
  - `repositories/`: acesso e manipulação dos dados no banco (TinyDB)
  - `schemas/`: validação e serialização de dados (Pydantic)
  - `core/`: configurações e logging centralizado
  - `db/`: scripts utilitários para o banco de dados
  - `models/`: modelos de domínio (entidades)

- **Singleton para o banco**: O acesso ao TinyDB é centralizado em um singleton, garantindo que toda a aplicação utilize a mesma instância do banco, evitando corrupção de dados e facilitando o controle de acesso.

- **Separação de responsabilidades**: Cada camada tem uma responsabilidade única, tornando o código mais legível, testável e fácil de modificar.

- **Logging centralizado**: Todas as operações relevantes são registradas em logs, facilitando o diagnóstico de problemas e auditoria.

- **Testes automatizados**: O projeto possui testes unitários cobrindo as principais regras de negócio e automação, incentivando o desenvolvimento orientado a testes (TDD).

- **Formatação e padrão PEP 8**: O uso do Black garante que todo o código siga o padrão oficial de estilo Python, facilitando a colaboração em equipe.

> **Dica para desenvolvedores iniciantes:**
> Explore cada camada do projeto para entender como as responsabilidades estão separadas. Isso é fundamental para trabalhar em projetos profissionais e crescer como desenvolvedor Python!

## Dúvidas ou problemas?
- Consulte a documentação do FastAPI: https://fastapi.tiangolo.com/
- Consulte a documentação do TinyDB: https://tinydb.readthedocs.io/
- Consulte a documentação do Selenium: https://selenium-python.readthedocs.io/

---

**Projeto desenvolvido para o desafio técnico da Fidelity Pesquisas Cadastrais.**
