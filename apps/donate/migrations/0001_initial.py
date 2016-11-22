# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 15:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('donor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_offers', to='login.User')),
                ('foodbank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_requests', to='login.User')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created', to='login.User')),
            ],
        ),
    ]
