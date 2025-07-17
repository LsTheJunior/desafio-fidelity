import pytest
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)


def test_read_pesquisas_empty(monkeypatch):
    # Mock get_pesquisas para retornar vazio
    with patch("app.crud.get_pesquisas", return_value=[]):
        response = client.get("/pesquisas")
        assert response.status_code == 200
        assert response.json() == []


def test_executa_pesquisa(monkeypatch):
    # Mock SPVAutomatico.pesquisa para não executar Selenium
    with patch("app.automation.SPVAutomatico.pesquisa", return_value=None):
        response = client.post("/executa-pesquisa", json={"filtro": 0})
        assert response.status_code == 200
        assert "status" in response.json()
