# Generated by Django 5.0.2 on 2024-03-03 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_transaksi_selesai'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaksi',
            name='selesai',
        ),
    ]
