import pytest

from droids.models import Peca


@pytest.fixture(scope='function')
def add_peca():
    def _add_peca(codigo, descricao, urgente):
        peca = Peca.objects.create(codigo=codigo, descricao=descricao, urgente=urgente)
        return peca
    return _add_peca
