# Generated by Django 4.0.3 on 2024-02-27 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='account_type',
            field=models.CharField(choices=[('admin', 'Admin'), ('petugas', 'Petugas'), ('pimpinan', 'Pimpinan')], max_length=20),
        ),
    ]
