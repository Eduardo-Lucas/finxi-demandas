# Generated by Django 3.0.5 on 2020-12-13 21:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('droids', '0006_demanda'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demanda',
            name='anunciante',
        ),
        migrations.AddField(
            model_name='demanda',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
