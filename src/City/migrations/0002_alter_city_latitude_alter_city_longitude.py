# Generated by Django 4.2.6 on 2023-11-18 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('City', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='city',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
    ]