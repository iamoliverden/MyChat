# Generated by Django 5.0.6 on 2024-06-21 03:18

import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyChatApp', '0002_alter_chat_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='chat',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=128, unique=True),
        ),
    ]
