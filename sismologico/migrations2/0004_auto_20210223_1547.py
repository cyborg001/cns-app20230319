# Generated by Django 3.1.6 on 2021-02-23 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sismologico', '0003_auto_20210223_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sismo',
            name='focalInfo',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='sismo',
            name='gapInfo',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]