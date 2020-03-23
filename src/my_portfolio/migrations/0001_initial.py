# Generated by Django 2.2.10 on 2020-03-23 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyPortfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(choices=[('Django', 'Django'), ('HTML/CSS', 'HTML/CSS'), ('Joomla', 'Joomla'), ('Wordpress', 'Wordpress')], max_length=10)),
            ],
            options={
                'verbose_name': 'My Portfolio',
                'verbose_name_plural': 'My Portfolio',
            },
        ),
    ]