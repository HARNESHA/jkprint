# Generated by Django 4.1.2 on 2022-10-21 11:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='costing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ply', models.IntegerField()),
                ('liner', models.IntegerField()),
                ('printing', models.CharField(max_length=20)),
                ('decale', models.FloatField()),
                ('cutting', models.IntegerField()),
                ('gsm', models.IntegerField()),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='newuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=12)),
                ('city', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField()),
            ],
        ),
    ]