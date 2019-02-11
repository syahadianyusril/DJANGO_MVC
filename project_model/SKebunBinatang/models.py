from django.db.models import CharField
from django.db.models import TextField
from django.db.models import IntegerField
from django.utils import timezone

from django.db import models as models
# Create your models here.

class Hewan(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=50)
    berat = models.CharField(max_length=50)
    umur = models.IntegerField()

    def __str__(self):
        return self.name

class Kandang(models.Model):
    name = models.CharField(max_length=255)
    isi_kandang = models.IntegerField()
    luas_kandang = models.IntegerField()

    def __str__(self):
        return self.name

class Penjaga(models.Model):
    name = models.CharField(max_length=255)
    nomor_telepon = models.IntegerField()
    jadwal_jaga = models.TextField(max_length=255)

    def __str__(self):
        return self.name

class Pengunjung(models.Model):
    name = models.CharField(max_length=255)
    nomor_telepon = models.IntegerField()
    hari_berkunjung = models.CharField(max_length=255)

    def __str__(self):
        return self.name