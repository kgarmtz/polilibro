# Generated by Django 3.2.7 on 2021-09-07 01:50

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_section_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Content'),
        ),
    ]
