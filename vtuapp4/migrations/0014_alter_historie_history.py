# Generated by Django 4.2.7 on 2024-09-24 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtuapp4', '0013_remove_users_userss_historie_userss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historie',
            name='history',
            field=models.CharField(default='no trasaction yet', max_length=100),
        ),
    ]