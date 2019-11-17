# Generated by Django 2.2.6 on 2019-11-11 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APISettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=30)),
                ('unique_name', models.CharField(max_length=50, unique=True)),
                ('url', models.URLField()),
                ('port', models.IntegerField()),
                ('path', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Endpoint',
                'verbose_name_plural': 'Endpoints',
                'db_table': 'APISettings',
            },
        ),
        migrations.CreateModel(
            name='EnvironmentPorts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=20)),
                ('unique_name', models.CharField(max_length=10, unique=True)),
                ('port', models.CharField(max_length=6)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Environment',
                'verbose_name_plural': 'Environment',
                'db_table': 'Environment',
            },
        ),
        migrations.CreateModel(
            name='UISettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=50)),
                ('unique_name', models.CharField(max_length=50, unique=True)),
                ('encoded_url', models.URLField()),
                ('url', models.URLField()),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'UI Setting',
                'verbose_name_plural': 'UI Settings',
                'db_table': 'UISettings',
            },
        ),
        migrations.CreateModel(
            name='WebHook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('1', 'Active'), ('2', 'In-active')], default='2', max_length=2)),
                ('status_code', models.CharField(max_length=3)),
                ('url', models.URLField()),
                ('fail_url', models.URLField()),
                ('success_url', models.URLField()),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'WebHook',
                'verbose_name_plural': 'WebHooks',
                'db_table': 'WebHookSettings',
            },
        ),
    ]