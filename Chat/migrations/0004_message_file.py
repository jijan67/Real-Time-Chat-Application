# Generated by Django 5.1.4 on 2024-12-28 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0003_message_is_read_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='chat_files/'),
        ),
    ]
