# Generated by Django 2.1.5 on 2019-02-21 03:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20190221_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoriteitem',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
