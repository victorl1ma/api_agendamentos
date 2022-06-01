from pyexpat import model
from rest_framework import serializers
from agendamentos.models import Agendamentos
from historicos.api.serializers import HistoricosDetalhesSerializer


class AgendamentosSerializers (serializers.ModelSerializer):
    class Meta:
        model = Agendamentos
        fields = '__all__'
class AgendamentosDetalhesSerializer (serializers.ModelSerializer):
    historicos = HistoricosDetalhesSerializer(many = True, read_only = True)
    class Meta:
        model = Agendamentos
        fields = [
            'id_agendamento', 
            'data_hora',
            'data_criacao',
            'cancelado',
            'obs',
            'tipo',
            'historicos'
        ]