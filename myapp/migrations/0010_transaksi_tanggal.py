# Generated by Django 5.0.2 on 2024-03-01 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_transaksi_pembayaran'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaksi',
            name='tanggal',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
