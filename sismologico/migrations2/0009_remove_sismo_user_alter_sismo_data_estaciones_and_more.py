# Generated by Django 4.1.7 on 2023-03-19 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sismologico', '0008_auto_20210410_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sismo',
            name='user',
        ),
        migrations.AlterField(
            model_name='sismo',
            name='data_estaciones',
            field=models.TextField(blank=True, default='', max_length=6144),
        ),
        migrations.AlterField(
            model_name='sismo',
            name='magC',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='sismo',
            name='magL',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='sismo',
            name='magW',
            field=models.FloatField(blank=True),
        ),
    ]
