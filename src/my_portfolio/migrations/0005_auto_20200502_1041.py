# Generated by Django 2.2.10 on 2020-05-02 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0004_auto_20200502_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myportfolio',
            name='items',
            field=models.CharField(choices=[('Python/Django', 'Python/Django'), ('HTML/CSS', 'HTML/CSS'), ('Joomla', 'Joomla'), ('Wordpress', 'Wordpress'), ('PyQt5', 'PyQt5')], max_length=10),
        ),
    ]