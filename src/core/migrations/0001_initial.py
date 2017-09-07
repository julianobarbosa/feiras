# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 18:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('cod_distrito', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('des_distrito', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feira',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('long', models.CharField(max_length=100)),
                ('lat', models.CharField(max_length=100)),
                ('setcens', models.CharField(max_length=100)),
                ('areap', models.CharField(max_length=100)),
                ('regiao5', models.CharField(choices=[('1', 'Leste'), ('2', 'Oeste'), ('3', 'Norte'), ('4', 'Centro'), ('5', 'Sul')], max_length=1)),
                ('regiao8', models.CharField(choices=[('1', 'Leste 1'), ('2', 'Oeste'), ('3', 'Norte 1'), ('4', 'Centro'), ('5', 'Sul 1'), ('6', 'Sul 2')], max_length=1)),
                ('nome_feira', models.CharField(max_length=200)),
                ('registro', models.CharField(max_length=200)),
                ('logradouro', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=200)),
                ('bairro', models.CharField(max_length=200)),
                ('referencia', models.CharField(max_length=200)),
                ('coddist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Distrito')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubPrefeitura',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('cod_subprefeitura', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('des_subprefeitura', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='feira',
            name='codsubpref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.SubPrefeitura'),
        ),
    ]