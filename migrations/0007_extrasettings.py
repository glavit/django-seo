# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 08:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('seo', '0006_auto_20160318_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('key', models.CharField(max_length=128, verbose_name='Key')),
                ('type', models.CharField(choices=[(b'text', 'Text'), (b'string', 'String'), (b'int', 'Integer'), (b'double', 'Double'), (b'file', 'File')], max_length=32, verbose_name='Type')),
                ('value', models.FileField(blank=True, max_length=20000, null=True, upload_to=b'', verbose_name='Value')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra_settings', to='sites.Site', verbose_name='Site')),
            ],
        ),
    ]
