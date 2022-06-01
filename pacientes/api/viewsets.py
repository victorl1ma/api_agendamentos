from pacientes.api.serializers import PacientesDetalhesSerializer, PacientesSerializers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from pacientes.models import Pacientes

class PacientesViewsSet(viewsets.ModelViewSet):
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializers

    @action(detail=True, methods=['get'])
    def detalhes (self, request, pk=None, *args, **kwargs):
        queryset = Pacientes.objects.filter(pk=pk)
        self.serializer_class = PacientesDetalhesSerializer
        serializer = self.get_serializer(queryset,many=True)

        return Response(serializer.data)
