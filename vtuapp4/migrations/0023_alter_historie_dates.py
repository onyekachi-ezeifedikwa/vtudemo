# Generated by Django 4.2.7 on 2024-09-28 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtuapp4', '0022_remove_historie_date_historie_dates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historie',
            name='dates',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
