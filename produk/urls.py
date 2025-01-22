from django.urls import path, re_path

from . import views

app_name = 'produks'

urlpatterns = [
    path('', views.produk_list, name='produk_list'),
    path('get/', views.get_produk, name='get_produk'),
    path('create/', views.produk_create, name='produk_create'),
    re_path(r'^(?P<pk>\d+)/$', views.produk_detail, name='produk_detail'),
    re_path(r'^(?P<pk>\d+)/update/$', views.produk_update, name='produk_update'),
    re_path(r'^(?P<pk>\d+)/delete/$', views.produk_delete, name='produk_delete'),
]
