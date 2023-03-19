# Generated by Django 3.0.6 on 2021-03-16 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sismologico', '0004_auto_20210223_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='sismo',
            name='analista',
            field=models.CharField(default='', max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]
