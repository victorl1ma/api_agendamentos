
from agendamentos.api.serializers import AgendamentosDetalhesSerializer, AgendamentosSerializers
from agendamentos.models import Agendamentos
from pacientes.models import Pacientes
from rest_framework import serializers


class PacientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '__all__'
class PacientesDetalhesSerializer(serializers.ModelSerializer):
    agendamentos = AgendamentosDetalhesSerializer(many=True, read_only = True)

    class Meta:
        model = Pacientes
        fields = [
            'id_paciente',
            'nome',
            'data_nascimento',
            'endereco',
            'num_endereco', 
            'cep',
            'data_cadastro',
            'rg',
            'agendamentos' 
        ]