# Generated by Django 4.2.7 on 2024-09-27 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtuapp4', '0021_historie_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historie',
            name='date',
        ),
        migrations.AddField(
            model_name='historie',
            name='dates',
            field=models.DateTimeField(auto_created=True, default=None, null=True),
        ),
    ]