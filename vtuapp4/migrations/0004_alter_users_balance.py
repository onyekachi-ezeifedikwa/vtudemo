# Generated by Django 4.2.7 on 2024-09-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtuapp4', '0003_alter_users_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='balance',
            field=models.FloatField(blank=True, default=0.0, verbose_name='balance'),
        ),
    ]
