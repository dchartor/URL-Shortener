# Generated by Django 2.2.1 on 2019-05-09 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='author',
            new_name='user',
        ),
    ]
