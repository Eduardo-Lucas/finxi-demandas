import pytest

from droids.models import Peca


@pytest.mark.django_db
def test_peca_model():
    peca = Peca(codigo="12345678", descricao="Rebimboca da Parafuseta", urgente="Sim")
    peca.save()
    assert peca.codigo == "12345678"
    assert peca.descricao == "Rebimboca da Parafuseta"
    assert peca.urgente == "Sim"
    assert peca.data_cadastro
    assert peca.data_alteracao
    assert str(peca) == peca.descricao
