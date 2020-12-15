from rest_framework import serializers
from .models import Peca, Anunciante, Demanda, User


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

    user = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=User.objects.all()
    )

    peca = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Peca.objects.all()
    )

    class Meta:
        model = Demanda
        fields = ('id', 'user', 'peca', 'status')
        read_only_fields = ('id', )
