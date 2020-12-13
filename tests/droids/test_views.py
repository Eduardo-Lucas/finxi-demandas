import json

import pytest

from droids.models import Peca


@pytest.mark.django_db
def test_add_peca(client):
    """This is the happy path, where everything is ok."""
    pecas = Peca.objects.all()
    assert len(pecas) == 0

    resp = client.post(
        "/api/pecas/",
        {
            "codigo": "12345678",
            "descricao": "Rebimboca da Parafuseta",
            "urgente": "Não",
        },
        content_type="application/json"
    )
    assert resp.status_code == 201
    assert resp.data["descricao"] == "Rebimboca da Parafuseta"

    pecas = Peca.objects.all()
    assert len(pecas) == 1


@pytest.mark.django_db
def test_add_peca_invalid_json(client):
    """Here, a paylod is not sent"""
    pecas = Peca.objects.all()
    assert len(pecas) == 0

    resp = client.post(
        "/api/pecas/",
        {},
        content_type="application/json"
    )
    assert resp.status_code == 400

    pecas = Peca.objects.all()
    assert len(pecas) == 0


@pytest.mark.django_db
def test_add_peca_invalid_json_keys(client):
    """Now, the payload is invalid -- i.e., the JSON object is empty or it contains the wrong keys"""
    pecas = Peca.objects.all()
    assert len(pecas) == 0

    resp = client.post(
        "/api/pecas/",
        {
            "codigo": "12345678",
            "genre": "Rebimboca da Parafuseta",
        },
        content_type="application/json"
    )
    assert resp.status_code == 400

    pecas = Peca.objects.all()
    assert len(pecas) == 0


@pytest.mark.django_db
def test_get_single_peca(client, add_peca):
    peca = add_peca(codigo="246802", descricao="Chave da Cruzeta externa", urgente="Não")
    resp = client.get(f"/api/pecas/{peca.id}/")
    assert resp.status_code == 200
    assert resp.data["descricao"] == "Chave da Cruzeta externa"


def test_get_single_peca_incorrect_id(client):
    resp = client.get(f"/api/pecas/foo/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_all_pecas(client, add_peca):
    peca_one = add_peca(codigo="35791", descricao="Parafuso Externo", urgente="Sim")
    peca_two = add_peca("579113", "Roda sobressalente", "Não")
    resp = client.get(f"/api/pecas/")
    assert resp.status_code == 200
    assert resp.data[0]["descricao"] == peca_one.descricao
    assert resp.data[1]["descricao"] == peca_two.descricao