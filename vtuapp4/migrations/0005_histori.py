# Generated by Django 4.2.7 on 2024-09-22 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtuapp4', '0004_alter_users_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='histori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200)),
            ],
        ),
    ]