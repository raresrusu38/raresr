# Generated by Django 2.2.10 on 2020-05-02 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0015_auto_20200322_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytechnicalskills',
            name='programing_language',
            field=models.CharField(choices=[('HMTL', 'HTML'), ('CSS', 'CSS'), ('JavaScript/jQuery', 'JavaScript/jQuery'), ('Ajax', 'Ajax'), ('Python/Django', 'Python/Django'), ('Joomla/Wordpress', 'Joomla/Wordpress'), ('Python/PyQt5', 'Pyhton/PyQt5')], max_length=20),
        ),
    ]
