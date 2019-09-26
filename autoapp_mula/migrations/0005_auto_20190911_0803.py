# Generated by Django 2.2.2 on 2019-09-11 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoapp_mula', '0004_auto_20190910_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='UISettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=30)),
                ('unique_name', models.CharField(max_length=10, unique=True)),
                ('encoded_url', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=200)),
            ],
            options={
                'verbose_name': 'UI',
                'verbose_name_plural': 'UI',
                'db_table': 'UISettings',
            },
        ),
        migrations.RenameField(
            model_name='apisettings',
            old_name='path',
            new_name='encoded_url',
        ),
        migrations.AlterField(
            model_name='apisettings',
            name='unique_name',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
