# Generated by Django 4.2.7 on 2024-09-23 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vtuapp4', '0012_rename_users_users_userss'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='userss',
        ),
        migrations.AddField(
            model_name='historie',
            name='userss',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]