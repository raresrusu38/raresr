from django.db import models
from django.urls import reverse

CATEGORIES = (
    ('Python/Django', 'Python/Django'),
    ('HTML/CSS', 'HTML/CSS'),
    ('Joomla', 'Joomla'),
    ('Wordpress', 'Wordpress'),
    ('PyQt5', 'PyQt5')
)

class MyPortfolio(models.Model):

    items              = models.CharField(max_length=10, choices=CATEGORIES)

    def __str__(self):
        return self.items

    class Meta:
        verbose_name        = ('My Portfolio')
        verbose_name_plural = ('My Portfolio')
