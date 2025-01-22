from .models import Produk
from django import forms


class ProdukForm(forms.ModelForm):

    class Meta:
        model = Produk
        fields = "__all__"


class InputForm(forms.Form):
    username = forms.CharField(max_length=100, initial="tesprogrammer220125C10")
    password = forms.CharField(max_length=100, initial="1612b37ba7f55b4a7fc2a528c2521d15")
