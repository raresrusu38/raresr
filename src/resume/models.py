from django.db import models
from django.urls import reverse

class Education(models.Model):
    title                   = models.CharField(max_length=50, blank=True)
    location                = models.CharField(max_length=50, blank=True)
    start_year              = models.PositiveSmallIntegerField(blank=True, null=True)
    stop_year               = models.PositiveSmallIntegerField(blank=True, null=True)
    description             = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name        = ('Education')
        verbose_name_plural = ('Educations')

class Experience(models.Model):
    title                   = models.CharField(max_length=50, blank=True)
    location                = models.CharField(max_length=50, blank=True)
    department              = models.CharField(max_length=50, blank=True)
    start_year              = models.PositiveSmallIntegerField(blank=True, null=True)
    stop_year               = models.PositiveSmallIntegerField(blank=True, null=True)
    description             = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name        = ('Experience')
        verbose_name_plural = ('Experiences')

    def get_absolute_url(self):
        return reverse('resume-detail', kwargs={
                'id': self.id,
            })

LANGUAGE = (
    ('Romanian', 'Romanian'),
    ('English', 'English'),
    ('Spanish', 'Spanish')
)

class MyLanguageSkills(models.Model):
    language                = models.CharField(max_length=10, choices=LANGUAGE)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = ('My Language Skills')
        verbose_name_plural = ('My Languages Skills')

PROGRAMING = (
    ('HMTL', 'HTML'),
    ('CSS', 'CSS'),
    ('JavaScript/jQuery', 'JavaScript/jQuery'),
    ('Ajax', 'Ajax'),
    ('Python/Django', 'Python/Django'),
    ('Joomla/Wordpress', 'Joomla/Wordpress')
)

class MyTechnicalSkills(models.Model):
    programing_language = models.CharField(max_length=20, choices=PROGRAMING)

    def __str__(self):
        return self.programing_language

    class Meta:
        verbose_name = ('My Technical Skills')
        verbose_name_plural = ('My Technical Skills')

