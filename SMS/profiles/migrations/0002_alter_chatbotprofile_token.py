# Generated by Django 3.2.11 on 2022-02-04 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatbotprofile',
            name='token',
            field=models.CharField(default='7fb7568cf78869a6337eda1336f5aadf18fc39ff', max_length=100),
        ),
    ]