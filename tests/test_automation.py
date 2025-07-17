"""
Testes para a classe SPVAutomatico responsável pela automação de consultas no sistema SPV.

Este módulo utiliza pytest e unittest.mock para validar o comportamento dos métodos de automação,
principalmente a checagem de resultados e o carregamento de sites mockados.
"""

import pytest
from app.automation import SPVAutomatico
from unittest.mock import patch, MagicMock


def test_checa_resultado_nada_consta():
    """
    Testa se o método checaResultado retorna 1 quando não existem informações disponíveis para os parâmetros informados.
    """
    assert (
        SPVAutomatico.checaResultado(
            "Não existem informações disponíveis para os parâmetros informados.", "123"
        )
        == 1
    )


def test_checa_resultado_consta_criminal():
    """
    Testa se o método checaResultado retorna 2 quando há processos encontrados na área criminal.
    """
    site = "Processos encontrados Criminal"
    assert SPVAutomatico.checaResultado(site, "123") == 2


def test_checa_resultado_consta_civel():
    """
    Testa se o método checaResultado retorna 5 quando há audiências (área cível).
    """
    site = "Audiências"
    assert SPVAutomatico.checaResultado(site, "123") == 5


def test_carrega_site_mocked():
    """
    Testa se o método carregaSite retorna o conteúdo da página mockada ao simular o navegador Edge.
    """
    with patch("app.automation.webdriver.Edge") as mock_browser:
        mock_instance = MagicMock()
        mock_instance.page_source = "mocked page"
        mock_browser.return_value = mock_instance
        result = SPVAutomatico.carregaSite(0, "doc")
        assert result == "mocked page"
