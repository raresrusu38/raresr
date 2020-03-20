from django.db import models

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
    start_year              = models.PositiveSmallIntegerField(blank=True, null=True)
    stop_year               = models.PositiveSmallIntegerField(blank=True, null=True)
    description             = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name        = ('Experience')
        verbose_name_plural = ('Experiences')

    

