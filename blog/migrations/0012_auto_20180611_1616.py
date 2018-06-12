# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-11 19:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0011_auto_20180611_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('matricula', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=120)),
                ('dt_nasc', models.DateField()),
                ('cpf', models.IntegerField()),
                ('telefone', models.IntegerField()),
                ('ender', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Atendente',
            fields=[
                ('nome', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('dt_nasc', models.DateField()),
                ('cpf', models.IntegerField()),
                ('tel', models.IntegerField()),
                ('ender', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('cod_emp', models.IntegerField(primary_key=True, serialize=False)),
                ('dt_emp', models.DateField()),
                ('cod_at', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Atendente')),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('nome', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('isbn', models.IntegerField()),
                ('desc', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='cod_li',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Livro'),
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='matricula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Aluno'),
        ),
    ]
