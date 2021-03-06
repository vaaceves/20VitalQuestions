# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-04 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_question_pdf_link_spa'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='issuu_eng',
            field=models.URLField(default=b'https://e.issuu.com/anonymous-embed.html?u=onelmedia&d=craig_groeschel', max_length=149),
        ),
        migrations.AddField(
            model_name='question',
            name='pdf_link_eng',
            field=models.URLField(default=b'https://gls-demo-f4707.firebaseapp.com/DISCUSSIONGUIDES/DISC01/Craig_Groeschel.pdf', max_length=349),
        ),
    ]
