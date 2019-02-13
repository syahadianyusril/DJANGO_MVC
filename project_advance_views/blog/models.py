from django.db.models import CharField
from django.db.models import TextField
from django.utils import timezone

from django.db import models as models

# Create your models here.

class Blog(models.Model):
    image = models.ImageField(upload_to = 'images')
    created_at = models.DateTimeField(default=timezone.now)
    judul = models.CharField(max_length=255)
    konten = models.TextField()

    def __str__(self):
        return self.judul