from django.contrib import admin

from .models import *

# Register your models here.
class KategoriAdmin(admin.ModelAdmin):

    list_display = ('id_kategori', 'nama_kategori')
    ordering = ['id_kategori']

class StatusAdmin(admin.ModelAdmin):

    list_display = ('id_status', 'nama_status')
    ordering = ['id_status']

class ProdukAdmin(admin.ModelAdmin):
    
    list_display = ('id_produk', 'nama_produk', 'harga', 'kategori', 'status')
    ordering = ['id_produk']

admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Produk, ProdukAdmin)

