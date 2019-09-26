# Generated by Django 2.2.2 on 2019-09-10 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoapp_mula', '0003_acknowledge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acknowledge',
            options={'verbose_name': 'Acknowledge', 'verbose_name_plural': 'Acknowledge'},
        ),
        migrations.AlterField(
            model_name='acknowledge',
            name='status',
            field=models.CharField(choices=[('1', 'Active'), ('2', 'In-active')], default='2', max_length=2),
        ),
    ]
