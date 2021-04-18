# Generated by Django 3.2 on 2021-04-18 02:42

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vessel_id', models.CharField(max_length=100, verbose_name='Vessel ID')),
                ('vessel_name', models.CharField(max_length=100, verbose_name='Vessel Name')),
                ('lon', models.FloatField(verbose_name='Longitude')),
                ('lat', models.FloatField(verbose_name='Latitude')),
                ('datetime', models.DateTimeField(verbose_name='Datetime')),
                ('length', models.FloatField(verbose_name='Length')),
                ('status', models.CharField(max_length=5, verbose_name='Status')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
