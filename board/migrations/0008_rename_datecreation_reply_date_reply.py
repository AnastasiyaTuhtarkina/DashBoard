# Generated by Django 5.1.1 on 2024-09-17 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_alter_post_author_alter_post_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='dateCreation',
            new_name='date_reply',
        ),
    ]
