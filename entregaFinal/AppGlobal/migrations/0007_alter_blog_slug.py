# Generated by Django 4.1.1 on 2022-10-17 15:19

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppGlobal', '0006_blog_slug_alter_blog_descripcion_alter_blog_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=True, populate_from='title'),
        ),
    ]