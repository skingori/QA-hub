# Generated by Django 2.2.2 on 2019-09-11 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoapp_mula', '0006_auto_20190911_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environmentports',
            name='description',
            field=models.TextField(max_length=20),
        ),
    ]
