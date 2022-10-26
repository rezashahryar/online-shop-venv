from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=2000)

    datetime_send = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    def __str__(self):
        return self.email
