# Generated by Django 5.0.4 on 2024-05-03 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trellobackend', '0003_alter_cards_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='workspace',
            name='members',
            field=models.CharField(default='me', max_length=255),
            preserve_default=False,
        ),
    ]
