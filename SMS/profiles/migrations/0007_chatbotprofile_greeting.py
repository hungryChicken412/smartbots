# Generated by Django 3.2.11 on 2022-02-19 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_chatbotprofile_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatbotprofile',
            name='greeting',
            field=models.TextField(default='Hi there! How Can I Help You!', max_length=1000),
        ),
    ]