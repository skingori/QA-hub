# Generated by Django 3.0.7 on 2020-07-08 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoapp_tingg', '0008_auto_20200708_0707'),
    ]

    operations = [
        migrations.AddField(
            model_name='uisettings',
            name='status',
            field=models.CharField(choices=[('1', 'Active'), ('2', 'In-active')], default='2', max_length=2),
        ),
        migrations.AlterField(
            model_name='uisettings',
            name='unique_name',
            field=models.CharField(max_length=50),
        ),
    ]
