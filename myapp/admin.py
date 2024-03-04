from django.contrib import admin
from myapp.models import *
from myapp.forms import SignUpForm
class CustomUserAdmin(admin.ModelAdmin):
    form = SignUpForm
    list_display = ['username', 'email']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Transaksi)