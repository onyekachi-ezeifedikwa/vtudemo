# Generated by Django 4.2.7 on 2024-09-22 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtuapp4', '0009_remove_users_user_historie_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='history',
            field=models.TextField(default='no trasaction yet'),
        ),
    ]