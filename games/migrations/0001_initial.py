# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 22:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_do_pobierania', models.CharField(max_length=200)),
                ('nazwa_gryy', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PaczkaGier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wydawca', models.CharField(max_length=250)),
                ('nazwa_paczki', models.CharField(max_length=100)),
                ('rodzaj_gier', models.CharField(max_length=100)),
                ('logo_gry', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='gra',
            name='paczka',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.PaczkaGier'),
        ),
    ]
