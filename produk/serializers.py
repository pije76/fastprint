from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import *


class ProdukSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(view_name='produk-detail')

	class Meta:
		model = Produk
		fields = ['id_produk', 'nama_produk', 'harga', 'kategori', 'status', 'detail']


	def to_representation(self, instance):
		rep = super().to_representation(instance)
		rep['kategori'] = instance.kategori.nama_kategori
		rep['status'] = instance.status.nama_status
		return rep
