# Generated by Django 3.0.4 on 2020-06-17 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autoapp_tingg', '0005_auto_20200616_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testraildetails',
            old_name='testrail_name',
            new_name='testrail_username',
        ),
    ]
