# Generated by Django 4.2.7 on 2024-09-21 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtuapp4', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=3),
        ),
    ]
