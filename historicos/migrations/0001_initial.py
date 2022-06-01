# Generated by Django 4.0.4 on 2022-05-30 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agendamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historicos',
            fields=[
                ('id_historico', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('aparecimentos_sintomas', models.CharField(blank=True, max_length=100, null=True)),
                ('duracao_sintomas', models.CharField(blank=True, max_length=100, null=True)),
                ('local_dor', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo_dor', models.CharField(blank=True, max_length=100, null=True)),
                ('conclusao', models.TextField(blank=True, null=True)),
                ('id_agendamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historicos', to='agendamentos.agendamentos')),
            ],
            options={
                'db_table': 'historicos',
                'managed': True,
            },
        ),
    ]
