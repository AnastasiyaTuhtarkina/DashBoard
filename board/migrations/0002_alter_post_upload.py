# Generated by Django 5.1.1 on 2024-09-11 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upload',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
    ]
