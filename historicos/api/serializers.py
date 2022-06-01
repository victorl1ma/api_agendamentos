from dataclasses import field
from pyexpat import model
from rest_framework import serializers

from historicos.models import Historicos
from imagens.api.serializers import ImagemnsHisotoricoSerializer
class HistoricosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historicos
        fields = '__all__'
class HistoricosDetalhesSerializer(serializers.ModelSerializer):
    imagens = ImagemnsHisotoricoSerializer(many=True,read_only=True)
    class Meta:
        model =Historicos
        fields = [
            'id_historico',
            'data',
            'id_agendamento',
            'aparecimentos_sintomas',
            'duracao_sintomas',
            'local_dor',
            'tipo_dor',
            'imagens'
        ]