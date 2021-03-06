# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-31 23:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('name', models.CharField(default='Enterprise Name', max_length=149)),
                ('contact_name', models.CharField(default='Client Name', max_length=149)),
                ('contact_phone', models.CharField(default='Client Phone', max_length=149)),
                ('contact_email', models.EmailField(default='contact@email.com', max_length=149)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('code', models.CharField(blank=True, max_length=149, null=True)),
                ('total_licenses', models.PositiveSmallIntegerField(default=1)),
                ('activated_licenses', models.PositiveSmallIntegerField(default=1)),
                ('client', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='client_license', to='licenses.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_code', models.CharField(blank=True, max_length=149, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
