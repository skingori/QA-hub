# Generated by Django 2.2.2 on 2019-09-11 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoapp_mula', '0005_auto_20190911_0803'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnvironmentPorts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=20)),
                ('unique_name', models.CharField(max_length=10, unique=True)),
                ('port', models.CharField(max_length=6)),
                ('description', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Environment',
                'verbose_name_plural': 'Environment',
                'db_table': 'Environment',
            },
        ),
        migrations.AlterModelOptions(
            name='uisettings',
            options={'verbose_name': 'UI Setting', 'verbose_name_plural': 'UI Settings'},
        ),
    ]
