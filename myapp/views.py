from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from myapp.models import *
from django.views.generic.edit import CreateView
from myapp.forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from myapp.decorators import role_required, guest
from django.http import HttpResponse
from myapp.resource import *
from django.shortcuts import render
from django.db.models import Sum
from datetime import datetime
from django.utils import timezone

# Mencari Data menggunkan id.
def search_view(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            try:
                search_results = [Transaksi.objects.get(id=int(search_query))]
            except (ValueError, Transaksi.DoesNotExist):
                search_results = []
            return render(request, 'user/search.html', {'search_results': search_results, 'query': search_query})
    else:
        form = SearchForm()
    return render(request, 'user/search.html', {'form': form})

#Mengexport data ke excel.
def export_xls(request):
    transaksi = TransaksiResources()
    dataset = transaksi.export()
    response = HttpResponse(dataset.xls, content_type="application/vnd.ms-excel")
    response['Content-Disposition'] = 'attachment; filename="transaksi.xls"'
    return response

#login sesuai role.
@method_decorator(guest, name="dispatch")
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = LoginForm()
        if request.POST.get('username')  and request.POST.get('username'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)          
            if user is not None:
                login(request, user)
                if user.account_type == 'admin':
                    return redirect('administrator')
                elif user.account_type == 'petugas':
                    return redirect('petugas')
                elif user.account_type == 'pimpinan':
                    return redirect('pimpinan')
                return redirect('halaman_user')
            else:
                return render(request, 'users/login.html', {'form': form})

#logout.
@method_decorator(login_required, name="dispatch") 
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('halaman_user')

#Menambahkan di urls jika diperlukan.
class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'users/tambah_user.html'
    success_url = '/administrator'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)
    
 


# admin crud.
@role_required('admin')
def tambah_transaksi(request):
    if request.method == 'POST':
        form = TransaksiForm(request.POST)
        if form.is_valid():
            data = form.save()
            return redirect('/struk/%s'% data.id) 
    else:
        form = TransaksiForm()
    return render(request, 'crud/tambah_transaksi.html', {'form': form})
#......
@role_required('admin')
def hapus_transaksi(request, id_transaksi):
    transaksi = Transaksi.objects.filter(id=id_transaksi)
    transaksi.delete()

    return redirect('/data_konsumen')
#........
@role_required('admin')
def ubah_transaksi(request, id_transaksi):
    transaksi = Transaksi.objects.get(id=id_transaksi)
    template = 'crud/ubah_transaksi.html'
    if request.POST:
        form = TransaksiForm(request.POST, instance=transaksi)
        if form.is_valid():
            form.save()
            return redirect('/data_konsumen', id_transaksi=id_transaksi)
    else:
        form = TransaksiForm(instance=transaksi)
        konteks = {
            'form':form,
            'transaksi':transaksi,
        }
    return render(request, 'crud/ubah_transaksi.html', konteks)





#  petugas crud.
@role_required('petugas')
def petugas_tambah_transaksi(request):
    if request.method == 'POST':
        form = TransaksiFormPetugas(request.POST)
        if form.is_valid():
            data = form.save()
            return redirect('/struk_petugas/%s'% data.id) 
    else:
        form = TransaksiFormPetugas()
    return render(request, 'crud/petugas_tambah_transaksi.html', {'form': form})
#......
@role_required('petugas')
def petugas_hapus_transaksi(request, id_transaksi):
    transaksi = Transaksi.objects.filter(id=id_transaksi)
    transaksi.delete()
    return redirect('/petugas_data_konsumen')
#......
@role_required('petugas')
def petugas_ubah_transaksi(request, id_transaksi):
    transaksi = Transaksi.objects.get(id=id_transaksi)
    template = 'crud/petugas_ubah_transaksi.html'
    if request.POST:
        form = TransaksiFormPetugas(request.POST, instance=transaksi)
        if form.is_valid():
            form.save()
            return redirect('/petugas_data_konsumen', id_transaksi=id_transaksi)
    else:
        form = TransaksiFormPetugas(instance=transaksi)
        konteks = {
            'form':form,
            'transaksi':transaksi,
        }
    return render(request, 'crud/petugas_ubah_transaksi.html', konteks)
@role_required('petugas')
def filter_petugas(request):
    datestr = request.GET['filter']
    date = datetime.strptime(datestr, '%Y-%m-%d').date()
    filter = Transaksi.objects.filter(datetime_published=datetime(date))
    return HttpResponse(request.GET['filter'])



# user.
def halaman_user(request):
    transaksi = Transaksi.objects.all()
    return render(request, 'user/halaman_user.html', {'transaksi': transaksi})



# Admin .
@login_required
@role_required('admin')
def administrator(request):
    total_users = CustomUser.objects.all().count()
    transaksi = Transaksi.objects.all()
    jumlah_transaksi = transaksi.count()
    user = CustomUser.objects.all()
    context = {
        'user': user,
        'total_users': total_users,
        'transaksi': transaksi,
        'jumlah_transaksi': jumlah_transaksi,
    }
    return render(request, 'admin/administrator.html', context)
#.......
@role_required('admin')
def data_konsumen(request):
    transaksi = Transaksi.objects.all()
    return render(request, 'admin/data_konsumen.html', {'transaksi': transaksi})
#........
@role_required('admin')
def data_petugas(request):
    petugas = CustomUser.objects.filter(account_type='petugas')
    return render(request, 'admin/data_petugas.html', {'petugas': petugas})
#........
@role_required('admin')
def jenis_layanan(request):
    transaksi = Transaksi.objects.all()
    return render(request, 'admin/jenis_layanan.html', {'transaksi': transaksi})
#.........
@role_required('admin')
def transaksi_order(request):
    transaksi = Transaksi.objects.all()
    return render(request, 'admin/transaksi_order.html', {'transaksi': transaksi})
#..........
@role_required('admin')
def history(request):
    transaksi = Transaksi.objects.all()
    return render(request, 'admin/history.html', {'transaksi': transaksi})
#...........
@role_required('admin')
def struk(request, id_transaksi):
   transaksi = Transaksi.objects.get(id=id_transaksi)
   return render(request, 'admin/struk.html', {'transaksi': transaksi})
#...........
@role_required('admin')
def laporan(request):
    transaksi = Transaksi.objects.all()
    return render(request, 'admin/laporan.html', {'transaksi': transaksi})



# Petugas.
@login_required
@role_required('petugas')
def petugas(request):
    transaksi = Transaksi.objects.all()
    jumlah_transaksi = transaksi.count()
    
    context = {
        'transaksi': transaksi,
        'jumlah_transaksi': jumlah_transaksi,
    }
    return render(request, 'petugas/petugas.html', context)
#...........
@role_required('petugas')
def petugas_data_konsumen(request):
    transaksi = Transaksi.objects.all()
    return render(request, 'petugas/petugas_data_konsumen.html', {'transaksi': transaksi})
#...........
@role_required('petugas')
def petugas_transaksi_order(request):
    transaksi = Transaksi.objects.all()
    if request.method == 'GET' and 'tanggal' in request.GET:
        date_str = request.GET.get('tanggal')
        date = timezone.make_aware(datetime.strptime(date_str, '%Y-%m-%d'))
        transaksi = Transaksi.objects.filter(tanggal__date=date)
    return render(request, 'petugas/petugas_transaksi_order.html', {'transaksi': transaksi})
#...........
@role_required('petugas')
def petugas_history(request):
    transaksi = Transaksi.objects.all()
    return render(request, 'petugas/petugas_history.html', {'transaksi': transaksi})
#...........
@role_required('petugas')
def struk_petugas(request, id_transaksi):
   transaksi = Transaksi.objects.get(id=id_transaksi)
   return render(request, 'petugas/struk_petugas.html', {'transaksi': transaksi})



# pimpinan.
@role_required('pimpinan')
def pimpinan(request):
    transaksi = Transaksi.objects.all()
    total_harga = Transaksi.objects.aggregate(total_harga=Sum('harga'))['total_harga']
    return render(request, 'pimpinan/pimpinan.html', {'transaksi': transaksi, 'total_harga': total_harga})
#...........
@role_required('pimpinan')
def pimpinan_history(request):
    transaksi = Transaksi.objects.all()
    return render(request, 'pimpinan/pimpinan_history.html', {'transaksi': transaksi})

  