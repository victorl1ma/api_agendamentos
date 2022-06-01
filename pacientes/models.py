from django.db import models

# Create your models here.
from django.db import models

def image_paciente(instance,filename):
    return '/'.join(['paciente',str(instance.nome),filename])

# Create your models here.
class Pacientes(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    image_selfie = models.ImageField(blank=True, null=True,upload_to=image_paciente)
    nome = models.CharField(max_length=100, blank=True, null=True)
    data_nascimento = models.DateTimeField(blank=True,null=True)
    endereco = models.CharField(max_length=80, blank=True,null=True)
    num_endereco = models.IntegerField(blank=True, null=True)
    cep = models.CharField(max_length=100, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    rg = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pacientes'