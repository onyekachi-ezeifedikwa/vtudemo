# Generated by Django 4.2.7 on 2024-09-22 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vtuapp4', '0006_rename_histori_historie'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vtuapp4.historie'),
        ),
    ]
