from django.db.models import CharField
from django.db.models import TextField
from django.db.models import IntegerField
from django.utils import timezone

from django.db import models as models
# Create your models here.

class Dokter(models.Model):
    name = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=50)
    bidang = models.CharField(max_length=50)
    jadwal_praktek = models.TextField(max_length=255)

    def __str__(self):
        return self.name

class Pasien(models.Model):
    name = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=50)
    alamat = models.TextField(max_length=255)
    keluhan = models.TextField(max_length=255)

    def __str__(self):
        return self.name

class Resep(models.Model):
    name = models.CharField(max_length=255)
    total_harga = models.IntegerField()
    kumpulan_obat = models.TextField(max_length=255)

    def __str__(self):
        return self.name

class Obat(models.Model):
    name = models.CharField(max_length=255)
    kandungan = models.TextField(max_length=255)
    khasiat = models.TextField(max_length=255)

    def __str__(self):
        return self.name