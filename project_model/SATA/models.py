from django.db.models import CharField
from django.db.models import TextField
from django.db.models import IntegerField
from django.utils import timezone

from django.db import models as models
# Create your models here.

class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    no_telepon = models.IntegerField()
    jabatan = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_lengkap

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    no_telepon = models.IntegerField()
    nomor_absen = models.IntegerField()
    nilai_rata = models.IntegerField()

    def __str__(self):
        return self.nama_lengkap

class Mata_Pelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=255)
    jadwal_dimulai = models.CharField(max_length=255)
    jadwal_berakhir = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nama_pelajaran

class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    no_telepon = models.IntegerField()
    mata_pelajaran = models.ForeignKey(Mata_Pelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_lengkap

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length=255)
    banyak_soal = models.IntegerField()
    bobot_nilai = models.IntegerField()
    mata_pelajaran = models.ForeignKey(Mata_Pelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_challenge

class Live_Code(models.Model):
    nama_live_code = models.CharField(max_length=255)
    banyak_soal = models.IntegerField()
    bobot_nilai = models.IntegerField()
    tanggal_pelaksanaan = models.DateTimeField(default=timezone.now)
    mata_pelajaran = models.ForeignKey(Mata_Pelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_live_code
