# Generated by Django 3.0.4 on 2020-06-16 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autoapp_tingg', '0004_testraildetails'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mockingdata',
            options={'verbose_name': 'Mocking Data', 'verbose_name_plural': 'Mocking Data'},
        ),
        migrations.AlterModelTable(
            name='mockingdata',
            table='MockingData',
        ),
    ]
