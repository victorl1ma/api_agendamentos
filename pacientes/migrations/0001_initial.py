# Generated by Django 4.0.4 on 2022-05-30 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('data_nascimento', models.DateTimeField(blank=True, null=True)),
                ('endereco', models.CharField(blank=True, max_length=80, null=True)),
                ('num_endereco', models.IntegerField(blank=True, null=True)),
                ('cep', models.CharField(blank=True, max_length=100, null=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('rg', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'pacientes',
                'managed': True,
            },
        ),
    ]
