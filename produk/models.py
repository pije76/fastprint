from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

numeric = RegexValidator(r'^[0-9+]', 'Only digit characters.')

# Create your models here.
class Kategori(models.Model):
    id_kategori = models.AutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_kategori

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategori"



class Status(models.Model):
    id_status = models.AutoField(primary_key=True)
    nama_status = models.CharField(max_length=20)

    def __str__(self):
        return self.nama_status

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"


class Produk(models.Model):
    id_produk = models.AutoField(primary_key=True)
    nama_produk = models.CharField(max_length=200, null=False, blank=False)
    harga = models.CharField(max_length=12, validators=[numeric])
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_produk

    class Meta:
        verbose_name = "Produk"
        verbose_name_plural = "Produk"

