from django.db import models


class Contact(models.Model):
    name        = models.CharField(max_length=25)
    email       = models.EmailField()
    phone       = models.CharField(max_length=12)
    message     = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name + "-" +  self.email

    class Meta:
        verbose_name = ('Contact')
        verbose_name_plural = ('Contacts')
