# Generated by Django 2.1.5 on 2020-03-20 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20200320_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='location',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
