from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views
from myapp.views import *

urlpatterns = [
    # URL untuk Admin
    path('admin/', admin.site.urls, name='admin'),  # Antarmuka Admin
    
    # URL untuk Pengguna
    path('halaman_user/', views.halaman_user, name='halaman_user'),  # Dasbor Pengguna
    
    # URL untuk Admin
    path('administrator/', views.administrator, name='administrator'),  # Dasbor Admin
    path('data_konsumen/', views.data_konsumen, name='data_konsumen'),  # Kelola data konsumen
    path('data_petugas/', views.data_petugas, name='data_petugas'),  # Kelola data petugas
    path('jenis_layanan/', views.jenis_layanan, name='jenis_layanan'),  # Jenis layanan
    path('transaksi_order/', views.transaksi_order, name='transaksi_order'),  # Transaksi pemesanan
    path('history/', views.history, name='history'),  # Riwayat transaksi
    path('laporan/', views.laporan, name='laporan'),  # Laporan
    path('struk/<int:id_transaksi>', views.struk, name='struk'),  # Struk transaksi
    path('export/xls', views.export_xls, name='export_xls'),  # Ekspor data ke Excel
    
    # URL untuk Petugas
    path('petugas/', views.petugas, name='petugas'),  # Dasbor Petugas
    path('petugas_data_konsumen/', views.petugas_data_konsumen, name='petugas_data_konsumen'),  # Kelola data konsumen oleh petugas
    path('petugas_transaksi_order/', views.petugas_transaksi_order, name='petugas_transaksi_order'),  # Transaksi pemesanan oleh petugas
    path('petugas_history/', views.petugas_history, name='petugas_history'),  # Riwayat transaksi oleh petugas
    path('struk_petugas/<int:id_transaksi>', views.struk_petugas, name='struk_petugas'),  # Struk transaksi oleh petugas
    path('filter_petugas/',views.filter_petugas, name='filter_petugas'),

    # URL untuk Pimpinan
    path('pimpinan/', views.pimpinan, name='pimpinan'),  # Dasbor Pimpinan
    path('pimpinan_history/', views.pimpinan_history, name='pimpinan_history'),  # Riwayat transaksi oleh pimpinan
    
    # URL CRUD untuk Admin
    path('tambah_transaksi/', tambah_transaksi, name='tambah_transaksi'),  # Tambah transaksi (Admin)
    path('transaksi/hapus/<int:id_transaksi>', hapus_transaksi, name="hapus_transaksi"),  # Hapus transaksi (Admin)
    path('transaksi/ubah/<int:id_transaksi>', ubah_transaksi, name="ubah_transaksi"),  # Ubah transaksi (Admin)
    
    # URL CRUD untuk Petugas
    path('petugas_tambah_transaksi/', petugas_tambah_transaksi, name='petugas_tambah_transaksi'),  # Tambah transaksi (Petugas)
    path('petugas_hapus_transaksi/hapus/<int:id_transaksi>', petugas_hapus_transaksi, name="petugas_hapus_transaksi"),  # Hapus transaksi (Petugas)
    path('petugas_ubah_transaksi/ubah/<int:id_transaksi>', petugas_ubah_transaksi, name="petugas_ubah_transaksi"),  # Ubah transaksi (Petugas)


    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('tambah_user/', views.SignUpView.as_view(), name='tambah_user'),



    path('search/', search_view, name='search_view'),
    
]





