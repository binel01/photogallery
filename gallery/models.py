from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    name = models.TextField(max_length='100')
    path = models.ImageField(upload_to='images')
    number_views = models.IntegerField(default=0)

    def __str__(self):
        return self.name
