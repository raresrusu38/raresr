# Generated by Django 2.2.10 on 2020-03-23 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20200323_2000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='comment',
            new_name='message',
        ),
    ]
