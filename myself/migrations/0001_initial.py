# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 22:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Skilltype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skilltitle', models.CharField(max_length=50)),
                ('skilldesc', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='skills',
            name='skilltype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myself.Skilltype'),
        ),
    ]