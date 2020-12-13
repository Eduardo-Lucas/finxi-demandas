from rest_framework import serializers
from .models import Peca


class PecaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Peca
        fields = '__all__'
        read_only_fields = ('id', 'data_cadastro', 'data_alteracao',)
