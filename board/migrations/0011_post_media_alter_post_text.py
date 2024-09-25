# Generated by Django 5.1.1 on 2024-09-25 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0010_remove_post_upload_alter_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]
