# Generated by Django 5.0.4 on 2024-05-01 15:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trellobackend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='columns',
            name='user',
        ),
        migrations.AddField(
            model_name='columns',
            name='workspace',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='trellobackend.workspace'),
        ),
    ]
