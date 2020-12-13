from rest_framework import serializers
from .models import Peca, Anunciante, Demanda


class PecaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Peca
        fields = '__all__'
        read_only_fields = ('id', 'data_cadastro', 'data_alteracao',)


class AnuncianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anunciante
        fields = '__all__'
        read_only_fields = ('id', )


class DemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demanda
        fields = '__all__'
        read_only_fields = ('id', )
