# Generated by Django 5.1.5 on 2025-01-21 17:12

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id_kategori', models.AutoField(primary_key=True, serialize=False)),
                ('nama_kategori', models.CharField(max_length=65, verbose_name='Kategori Produk')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id_status', models.AutoField(primary_key=True, serialize=False)),
                ('nama_status', models.CharField(max_length=65, unique=True, verbose_name='Status Produk')),
            ],
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id_produk', models.AutoField(primary_key=True, serialize=False)),
                ('nama_produk', models.CharField(max_length=200, verbose_name='Nama Produk')),
                ('harga', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^[0-9+]', 'Only digit characters.')])),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produk.kategori')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produk.status')),
            ],
        ),
    ]
