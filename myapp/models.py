from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password



class CustomUser(AbstractUser):
        
    ACCOUNT_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('petugas', 'Petugas'),
        ('pimpinan', 'Pimpinan'),
    )
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)



class Transaksi(models.Model):
    STATUS_CHOICES = (
        ('baru', 'Baru'),
        ('proses', 'Proses'),
        ('selesai', 'Selesai'),
        ('telah_diambil', 'Telah Diambil'),  
    )

    JENIS_LAYANAN_CHOICES = (
        ('ekspres', 'Ekspres'),
        ('normal', 'Normal'),
        ('hemat', 'Hemat'),
    )

    PEMBAYARAN_CHOICES = (
        ('lunas', 'Lunas'),
        ('belum_lunas', 'Belum Lunas'),  # Pilihan untuk pembayaran
    )

    JENIS_PEMBAYARAN_CHOICES = (
        ('cash', 'Cash'),
        ('debit', 'Debit'),
        ('paylater', 'Pay Later'),
    )

    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    nohp = models.CharField(max_length=15)
    perkilo = models.DecimalField(max_digits=10, decimal_places=2)
    jenis_layanan = models.CharField(max_length=100, choices=JENIS_LAYANAN_CHOICES)
    harga = models.DecimalField(max_digits=10, decimal_places=2)  
    jenis_pembayaran = models.CharField(max_length=100, choices=JENIS_PEMBAYARAN_CHOICES)
    pembayaran = models.CharField(max_length=100, choices=PEMBAYARAN_CHOICES)
    tanggal = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
   

    def __str__(self):
        return self.nama
