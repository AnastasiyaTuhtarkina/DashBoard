# Generated by Django 5.1.1 on 2024-09-11 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_category_remove_post_category_postcategory_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcategory',
            old_name='category',
            new_name='post_category',
        ),
    ]
