from django import forms
from myapp.models import *
from django.contrib.auth.forms import UserCreationForm


class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search')

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'account_type']
 
class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class Users(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__' 

class TransaksiForm(forms.ModelForm):
    class Meta:
        model = Transaksi
        fields = '__all__' 

class TransaksiFormPetugas(forms.ModelForm):
    class Meta:
        model = Transaksi
        exclude = ['pembayaran', 'jenis_layanan', 'jenis_pembayaran']