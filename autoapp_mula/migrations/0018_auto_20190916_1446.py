# Generated by Django 2.2.2 on 2019-09-16 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoapp_mula', '0017_auto_20190916_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apisettings',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='apisettings',
            name='path',
            field=models.CharField(max_length=200),
        ),
    ]