import pytest
from app.crud import get_pesquisas


def test_get_pesquisas_returns_list(tmp_path, monkeypatch):
    # Cria um banco TinyDB temporário
    from tinydb import TinyDB

    db_path = tmp_path / "db.json"
    db = TinyDB(db_path)
    pesquisas_table = db.table("pesquisas")
    pesquisas_table.insert_multiple(
        [{"cod_pesquisa": "1", "nome": "A"}, {"cod_pesquisa": "2", "nome": "B"}]
    )
    monkeypatch.setattr("app.crud.db", db)
    result = get_pesquisas(skip=0, limit=2)
    assert len(result) == 2
    assert result[0]["nome"] == "A"
    assert result[1]["nome"] == "B"
