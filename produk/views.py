from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from rest_framework import permissions, viewsets, status, generics
from rest_framework.decorators import api_view, action
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *

from .models import Produk, Kategori, Status
from .forms import ProdukForm, InputForm

import requests
import json

url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
	get_status = Status.objects.get(nama_status='bisa dijual')
	queryset = Produk.objects.filter(status=get_status.pk)
	serializer_class = ProdukSerializer


@csrf_exempt
def get_produk(request):

	if request.method == "POST":
		form = InputForm(request.POST)

		get_username = request.POST.get('username')
		get_password = request.POST.get('password')

		if form.is_valid():

			payload = {
				"username": get_username,
				"password": get_password,
			}
			headers = {'content-type': 'application/json'}
			session = requests.Session()
			response = session.post(url, data=payload)
			response = response.json()
			data = response['data']

			for item in data:
				id_produk = item["id_produk"]
				nama_produk = item["nama_produk"]
				harga = item["harga"]
				kategori = item["kategori"]
				status = item["status"]

				try:
					objk = Kategori.objects.get(nama_kategori=kategori)
				except Kategori.DoesNotExist:
					objk = Kategori(nama_kategori=kategori)
				objk.save()

				try:
					objs = Status.objects.get(nama_status=status)
				except Status.DoesNotExist:
					objs = Status(nama_status=status)
				objs.save()

				obj, created = Produk.objects.update_or_create(
					id_produk=id_produk,
					nama_produk=nama_produk,
					harga=harga,
					kategori=Kategori.objects.get(nama_kategori=kategori),
					status=Status.objects.get(nama_status=status),
				)
				print(Kategori.objects.get(nama_kategori=kategori))

			return redirect(reverse("produks:produk_list"))
		else:
			messages.warning(request, form.errors)
			return redirect(reverse("produks:produk_list"))

	else:
		form = InputForm()
		return render(request, "get_form.html", { "form": form, })


def produk_list(request):
	try:
		get_status = Status.objects.get(nama_status='bisa dijual')
		produks = Produk.objects.filter(status=get_status.pk)
	except Status.DoesNotExist:
		produks = Produk.objects.all()

	return render(request, "produk_list.html", { "produks": produks,})


@csrf_exempt
def produk_create(request):
	if request.method == "POST":
		form = ProdukForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(reverse("produks:produk_list"))
	else:
		form = ProdukForm()

	return render(request, "produk_form.html", { "form": form, })


def produk_detail(request, pk):
	produk = get_object_or_404(Produk, pk=pk)
	return render(request, "produk_detail.html", { "produk": produk, })


@csrf_exempt
def produk_update(request, pk):
	produk_obj = get_object_or_404(Produk, pk=pk)
	if request.method == 'POST':
		form = ProdukForm(instance=produk_obj, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect(reverse("produks:produk_detail", args=[pk,]))
	else:
		form = ProdukForm(instance=produk_obj)

	return render(request, "produk_form.html", { "form": form, "object": produk_obj})


def produk_delete(request, pk):
	produk_obj = get_object_or_404(Produk, pk=pk)
	produk_obj.delete()
	return redirect(reverse("produks:produk_list"))

