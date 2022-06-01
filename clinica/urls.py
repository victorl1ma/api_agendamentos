"""clinica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from agendamentos.api.viewsets import AgendamentosViewSet
from pacientes.api.viewsets import PacientesViewsSet
from historicos.api.viewsets import HistoricosViewSet
from rest_framework import routers
from imagens.api.viewsets import ImagensHistoricoViewSet

router = routers.DefaultRouter()

router.register('pacientes',PacientesViewsSet)
router.register('agendamentos',AgendamentosViewSet)
router.register('historicos',HistoricosViewSet)
router.register('imagens_historicos',ImagensHistoricoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
