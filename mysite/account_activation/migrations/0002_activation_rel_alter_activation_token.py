# Generated by Django 4.1 on 2022-09-04 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account_activation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activation',
            name='rel',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activation',
            name='token',
            field=models.CharField(max_length=200),
        ),
    ]
