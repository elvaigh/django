# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 19:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('adresse', models.TextField()),
                ('photo', models.ImageField(upload_to=b'photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Mote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MoteId', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=42)),
                ('board', models.CharField(max_length=42)),
                ('data', models.CharField(max_length=42)),
                ('viewed', models.DateTimeField(auto_now_add=True, verbose_name=b'Date de d\xc3\xa9ploiement')),
                ('moteChannel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sonsorMenager.Channel')),
            ],
        ),
    ]
