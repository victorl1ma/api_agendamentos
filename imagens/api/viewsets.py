from rest_framework import viewsets
from imagens.api.serializers import ImagemnsHisotoricoSerializer

from imagens.models import ImagensHistorico

class ImagensHistoricoViewSet(viewsets.ModelViewSet):
    queryset = ImagensHistorico.objects.all()
    serializer_class = ImagemnsHisotoricoSerializer