# Generated by Django 5.0.2 on 2024-03-01 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_transaksi_jenis_pembayaran_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaksi',
            name='jenis_pembayaran',
            field=models.CharField(choices=[('cash', 'Cash'), ('debit', 'Debit'), ('paylater', 'Pay Later')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]