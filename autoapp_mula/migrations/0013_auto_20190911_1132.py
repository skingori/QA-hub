# Generated by Django 2.2.2 on 2019-09-11 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoapp_mula', '0012_webhook_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uisettings',
            name='unique_name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
