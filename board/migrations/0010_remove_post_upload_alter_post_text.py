# Generated by Django 5.1.1 on 2024-09-25 08:46

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_userresponse_delete_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='upload',
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
    ]
