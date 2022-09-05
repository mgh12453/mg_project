# Generated by Django 4.1 on 2022-09-04 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('first_page', '0002_master'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master',
            name='is_maser',
        ),
        migrations.AddField(
            model_name='master',
            name='is_master',
            field=models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
