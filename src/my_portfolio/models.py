from django.db import models
from django.urls import reverse

CATEGORIES = (
    ('Django', 'Django'),
    ('HTML/CSS', 'HTML/CSS'),
    ('Joomla', 'Joomla'),
    ('Wordpress', 'Wordpress')
)

class MyPortfolio(models.Model):

    categories = models.CharField(max_length=10, choices=CATEGORIES)

    def __str__(self):
        return self.categories

    class Meta:
        verbose_name = ('My Portfolio')
        verbose_name_plural = ('My Portfolio')
