from django.db import models

class AboutMe(models.Model):
    title       = models.CharField(max_length=100)
    overview    = models.TextField()
    updated     = models.DateTimeField(auto_now=True)
    thumbnail   = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('About Me')
        verbose_name_plural = ('About Me')

