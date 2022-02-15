# Generated by Django 3.2.11 on 2022-02-04 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0002_alter_chatbotprofile_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatbotprofile',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Connected_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chatbotprofile',
            name='token',
            field=models.CharField(default='3838f94f8b4b862f9b65', max_length=100),
        ),
    ]