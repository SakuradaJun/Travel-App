# Generated by Django 2.2.5 on 2020-01-23 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20200123_0832'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='contact',
            new_name='author',
        ),
    ]
