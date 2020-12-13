# Generated by Django 3.0.5 on 2020-12-13 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('droids', '0003_auto_20201213_0554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anunciante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(blank=True, max_length=30, null=True)),
                ('celular', models.CharField(blank=True, max_length=20, null=True, verbose_name='Celular')),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('endereco', models.CharField(blank=True, max_length=60, null=True, verbose_name='Endereço')),
                ('complemento', models.CharField(blank=True, max_length=60, null=True, verbose_name='Complemento')),
                ('numero', models.CharField(blank=True, max_length=20, null=True, verbose_name='Número')),
                ('bairro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bairro')),
                ('cidade', models.CharField(blank=True, max_length=50, null=True)),
                ('cep', models.CharField(blank=True, max_length=9, null=True, verbose_name='CEP')),
                ('estado', models.CharField(blank=True, max_length=2, null=True, verbose_name='UF')),
                ('pais', models.CharField(blank=True, default='Brasil', max_length=50, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
