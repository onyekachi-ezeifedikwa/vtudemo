# Generated by Django 4.2.7 on 2024-09-24 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vtuapp4', '0014_alter_historie_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historie',
            name='userss',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL),
        ),
    ]
