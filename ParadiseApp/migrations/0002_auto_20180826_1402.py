# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-26 11:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ParadiseApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('format', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='roll',
            name='batch',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='roll',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='roll',
            name='remainder',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='roll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ParadiseApp.Roll'),
        ),
    ]