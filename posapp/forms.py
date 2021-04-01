from .models import *
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class SupplierForm(forms.ModelForm):
    # category = forms.CharField(widget=forms.TextInput())
    # publisher = forms.CharField(widget=forms.TextInput())
    # author = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Supplier
        fields = '__all__'