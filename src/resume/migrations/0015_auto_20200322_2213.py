# Generated by Django 2.2.10 on 2020-03-22 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0014_auto_20200322_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytechnicalskills',
            name='programing_language',
            field=models.CharField(choices=[('HMTL', 'HTML'), ('CSS', 'CSS'), ('JavaScript/jQuery', 'JavaScript/jQuery'), ('Ajax', 'Ajax'), ('Python/Django', 'Python/Django'), ('Joomla/Wordpress', 'Joomla/Wordpress')], max_length=20),
        ),
    ]
