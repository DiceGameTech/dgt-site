# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('article', '0001_initial'), ('article', '0002_auto_20161231_1714'), ('article', '0003_auto_20170117_0955'), ('article', '0004_auto_20170118_1153'), ('article', '0005_auto_20170130_1326'), ('article', '0006_auto_20170130_1427')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('subtitle', models.CharField(max_length=256, verbose_name='subtitle')),
                ('slug', models.SlugField(max_length=80, verbose_name='slug')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads/articles/thumbnail/', verbose_name='thumbnail')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('pub_date', models.DateTimeField(blank=True, null=True)),
                ('contents', models.TextField(verbose_name='contents')),
                ('authors', models.ManyToManyField(to='article.User', verbose_name='authors')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=256, verbose_name='firstname')),
                ('lastname', models.CharField(max_length=256, verbose_name='lastname')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=256, verbose_name='tag')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='article.Tag', verbose_name='tags'),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(default='game design', max_length=256, verbose_name='category')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='article.Category', verbose_name='category'),
        ),
    ]
