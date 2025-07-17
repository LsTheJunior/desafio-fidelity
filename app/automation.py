"""
Módulo de automação de consultas jurídicas utilizando Selenium e TinyDB.

Contém a classe SPVAutomatico responsável por executar automações no sistema SPV,
realizar consultas, processar resultados e interagir com o banco de dados.
Inclui configuração de logging e constantes para identificação de resultados.
"""

import datetime
import sys
import os
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
from tinydb import TinyDB, Query
from app.database import db
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

NADA_CONSTA = "Não existem informações disponíveis para os parâmetros informados."
CONSTA01 = "Processos encontrados"
CONSTA02 = "Audiências"
# Caminho para o msedgedriver.exe dentro da pasta app
EXECUTAVEL = os.path.join(os.path.dirname(__file__), "msedgedriver.exe")


class SPVAutomatico:
    def __init__(self, filtro=0):
        self.filtro = filtro
        logger.info(f"SPVAutomatico inicializado com filtro={filtro}")

    def conectaBD(self, filtro, skip=0, limit=210):
        logger.info(
            f"Buscando pesquisas no banco (filtro={filtro}, skip={skip}, limit={limit})"
        )
        pesquisas_table = db.table("pesquisas")
        PesquisaQ = Query()
        pesquisas = pesquisas_table.search(
            (PesquisaQ.tipo == "0") & (PesquisaQ.cpf != "")
        )
        pesquisas = [
            p
            for p in pesquisas
            if p.get("uf") == "SP"
            or p.get("cod_uf_nascimento") == "26"
            or p.get("cod_uf_rg") == "26"
        ]
        logger.info(f"Encontradas {len(pesquisas)} pesquisas válidas")
        return pesquisas[skip : skip + limit]

    def pesquisa(self, loop=True):
        w = 0
        tempo_inicio = datetime.datetime.now()
        filtro = self.filtro
        i = self.filtro
        qry = self.conectaBD(filtro)
        totPesquisas = len(qry)
        logger.info(f"Iniciando pesquisa: total de pesquisas={totPesquisas}")
        tentativas_sem_dados = 0
        while True:
            if totPesquisas > 0:
                for pesquisa in tqdm(qry):
                    logger.info(
                        f"Executando pesquisa para: {pesquisa.get('nome')} (CPF: {pesquisa.get('cpf')})"
                    )
                    try:
                        self.executaPesquisa(
                            filtro,
                            pesquisa.get("nome"),
                            pesquisa.get("cpf"),
                            pesquisa.get("rg"),
                            pesquisa.get("cod_pesquisa"),
                            None,
                        )
                    except Exception as e:
                        logger.error(f"Erro ao executar pesquisa: {e}")
                    tempo_fim = datetime.datetime.now()
                    tempo_gasto = round((tempo_fim - tempo_inicio).total_seconds(), 2)
                    if tempo_gasto >= 600:
                        logger.warning(
                            "Tempo limite atingido, interrompendo loop de pesquisas."
                        )
                        break
                tempo_gasto = 0
                i += 1
                if not loop:
                    logger.info("Execução única (sem loop) finalizada.")
                    break
                if i <= 3:
                    logger.info(f"RECOMENÇANDO COM O FILTRO {i}")
                    self.filtro = i
                    filtro = i
                    qry = self.conectaBD(filtro)
                    totPesquisas = len(qry)
                    continue
                else:
                    logger.info("Ciclo de filtros finalizado. Aguardando novos dados.")
                    time.sleep(60)
                    i = 0
                    self.filtro = 0
                    filtro = 0
                    qry = self.conectaBD(filtro)
                    totPesquisas = len(qry)
                    continue
            else:
                tentativas_sem_dados += 1
                logger.info(
                    f"Nenhuma pesquisa encontrada. Tentativa {tentativas_sem_dados}/20. Aguardando para tentar novamente."
                )
                if not loop:
                    logger.info("Execução única (sem loop) finalizada sem dados.")
                    break
                time.sleep(60)
                if tentativas_sem_dados >= 20:
                    logger.warning(
                        "20 tentativas sem dados. Aguardando 1 hora antes de tentar novamente."
                    )
                    time.sleep(3600)
                    tentativas_sem_dados = 0
                qry = self.conectaBD(filtro)
                totPesquisas = len(qry)

    def executaPesquisa(self, filtro, nome, cpf, rg, codPesquisa, spvTipo):
        pesquisas_spv = db.table("pesquisas_spv")
        logger.info(
            f"executaPesquisa: filtro={filtro}, nome={nome}, cpf={cpf}, rg={rg}, codPesquisa={codPesquisa}"
        )
        if filtro == 0 and cpf:
            site = self.carregaSite(filtro, cpf)
            result = self.checaResultado(site, codPesquisa)
            pesquisa_spv = {
                "cod_pesquisa": codPesquisa,
                "cod_spv": "1",
                "cod_spv_computador": "36",
                "cod_spv_tipo": None,
                "resultado": str(result),
                "cod_funcionario": "-1",
                "filtro": str(filtro),
                "website_id": "1",
            }
            pesquisas_spv.insert(pesquisa_spv)
            logger.info(f"Pesquisa SPV inserida para CPF {cpf}")
        elif filtro in [1, 3] and rg:
            site = self.carregaSite(filtro, rg)
            result = self.checaResultado(site, codPesquisa)
            pesquisa_spv = {
                "cod_pesquisa": codPesquisa,
                "cod_spv": "1",
                "cod_spv_computador": "36",
                "cod_spv_tipo": None,
                "resultado": str(result),
                "cod_funcionario": "-1",
                "filtro": str(filtro),
                "website_id": "1",
            }
            pesquisas_spv.insert(pesquisa_spv)
            logger.info(f"Pesquisa SPV inserida para RG {rg}")
        elif filtro == 2 and nome:
            site = self.carregaSite(filtro, nome)
            result = self.checaResultado(site, codPesquisa)
            pesquisa_spv = {
                "cod_pesquisa": codPesquisa,
                "cod_spv": "1",
                "cod_spv_computador": "36",
                "cod_spv_tipo": None,
                "resultado": str(result),
                "cod_funcionario": "-1",
                "filtro": str(filtro),
                "website_id": "1",
            }
            pesquisas_spv.insert(pesquisa_spv)
            logger.info(f"Pesquisa SPV inserida para nome {nome}")

    @staticmethod
    def checaResultado(site, codPesquisa):
        final_result = 7
        if NADA_CONSTA in site:
            final_result = 1
        elif (CONSTA01 in site or CONSTA02 in site) and (
            "Criminal" in site or "criminal" in site
        ):
            final_result = 2
        elif CONSTA01 in site or CONSTA02 in site:
            final_result = 5
        logging.info(
            f"checaResultado: codPesquisa={codPesquisa}, resultado={final_result}"
        )
        return final_result

    @staticmethod
    def carregaSite(filtro, documento):
        logging.info(f"Abrindo navegador para filtro={filtro}, documento={documento}")
        service = Service(executable_path=EXECUTAVEL)
        options = Options()
        options.add_argument("-headless")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        browser = webdriver.Edge(service=service, options=options)
        logging.info("Navegador Edge iniciado")
        browser.get("https://esaj.tjsp.jus.br/cpopg/open.do")
        logging.info("Página do TJSP carregada")
        if filtro in [0, 1, 3]:
            try:
                logging.info("Selecionando tipo de pesquisa: DOCPARTE")
                select_el = browser.find_element("xpath", '//*[@id="cbPesquisa"]')
                select_ob = Select(select_el)
                select_ob.select_by_value("DOCPARTE")
                logging.info("Preenchendo campo DOCPARTE")
                browser.find_element("xpath", '//*[@id="campo_DOCPARTE"]').send_keys(
                    documento
                )
                logging.info("Clicando em Consultar Processos")
                browser.find_element(
                    "xpath", '//*[@id="botaoConsultarProcessos"]'
                ).click()
            except Exception as e:
                logging.error(f"Erro ao carregar site (DOCPARTE): {e}")
                time.sleep(120)
                SPVAutomatico.restarta_programa()
        elif filtro == 2:
            try:
                logging.info("Selecionando tipo de pesquisa: NMPARTE")
                select_el = browser.find_element("xpath", '//*[@id="cbPesquisa"]')
                select_ob = Select(select_el)
                select_ob.select_by_value("NMPARTE")
                logging.info("Clicando em pesquisar por nome completo")
                browser.find_element(
                    "xpath", '//*[@id="pesquisarPorNomeCompleto"]'
                ).click()
                logging.info("Preenchendo campo NMPARTE")
                browser.find_element("xpath", '//*[@id="campo_NMPARTE"]').send_keys(
                    documento
                )
                logging.info("Clicando em Consultar Processos")
                browser.find_element(
                    "xpath", '//*[@id="botaoConsultarProcessos"]'
                ).click()
            except Exception as e:
                logging.error(f"Erro ao carregar site (NMPARTE): {e}")
                time.sleep(120)
                SPVAutomatico.restarta_programa()
        page_source = browser.page_source
        browser.quit()
        logging.info(f"Navegador fechado para documento={documento}")
        return page_source

    @staticmethod
    def restarta_programa():
        try:
            logging.info("Reiniciando o programa...")
            os.execv(sys.executable, [sys.executable] + sys.argv)
        except Exception as e:
            logging.error(f"PROGRAMA ENCERRADO: {e}")
            quit()


# Exemplo de uso:
# p = SPVAutomatico(0)
# p.pesquisa()
