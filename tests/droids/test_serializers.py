from unicodedata import decimal

from droids.serializers import PecaSerializer


def test_valid_peca_serializer():
    valid_serializer_data = {
        "codigo": "12345678",
        "descricao": "Rebimboca da Parafuseta",
        "urgente": "Sim"
    }
    serializer = PecaSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_movie_serializer():
    invalid_serializer_data = {
        "codigo": "12345678",
        "urgente": "Sim",
    }
    serializer = PecaSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"descricao": ["This field is required."]}
