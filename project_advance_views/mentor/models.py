from django.db.models import CharField
from django.db.models import TextField
from django.utils import timezone

from django.db import models as models

# Create your models here.

class Mentor(models.Model):
    image = models.ImageField(upload_to = 'images')
    name = models.CharField(max_length=255)
    experiences = models.TextField()
    quote = models.TextField()

    def __str__(self):
        return self.name