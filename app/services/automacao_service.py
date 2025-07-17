"""
Serviço de automação de pesquisas jurídicas via Selenium.

Executa a lógica de automação utilizando a classe SPVAutomatico, processando pesquisas conforme o filtro informado,
registrando logs detalhados e tratando exceções durante a execução em lote ou individual.
"""

from app.repositories.pesquisa_repository import PesquisaRepository
from app.core.logger import logger
from app.automation import SPVAutomatico


class AutomacaoService:
    def __init__(self, filtro):
        self.filtro = filtro
        self.repo = PesquisaRepository()

    def executar(self):
        pesquisas = self.repo.get_by_filtro(self.filtro)
        logger.info(
            f"Executando automação para filtro={self.filtro}, total={len(pesquisas)}"
        )
        spv = SPVAutomatico(self.filtro)
        for pesquisa in pesquisas:
            logger.info(f"Processando: {pesquisa['nome']} (CPF: {pesquisa['cpf']})")
            try:
                spv.executaPesquisa(
                    self.filtro,
                    pesquisa.get("nome"),
                    pesquisa.get("cpf"),
                    pesquisa.get("rg"),
                    pesquisa.get("cod_pesquisa"),
                    None,
                )
            except Exception as e:
                logger.error(f"Erro ao processar pesquisa: {e}")
        return {"executado": len(pesquisas)}

    @staticmethod
    def executar_todos():
        resultados = []
        for filtro in range(4):
            serv = AutomacaoService(filtro)
            resultados.append(serv.executar())
        return resultados
