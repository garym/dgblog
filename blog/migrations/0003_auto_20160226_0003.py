# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-26 00:03
from __future__ import unicode_literals

from django.db import migrations, models

def copy_text_to_text_markdown(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    for post in Post.objects.all():
        post.text_markdown = post.text
        post.save()

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_text_markdown'),
    ]

    operations = [
        migrations.RunPython(copy_text_to_text_markdown),
    ]
