# Generated by Django 5.0.2 on 2024-03-01 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_transaksi_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaksi',
            name='status',
            field=models.CharField(choices=[('baru', 'Baru'), ('proses', 'Proses'), ('selesai', 'Selesai'), ('telah_diambil', 'Telah Diambil')], max_length=100),
        ),
    ]
