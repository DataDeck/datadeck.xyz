# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=100)),
                ('slug', models.SlugField(null=True, editable=False, blank=True)),
                ('descripcion', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=100)),
                ('slug', models.SlugField(null=True, editable=False, blank=True)),
                ('descripcion', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('barcode', models.PositiveIntegerField(null=True, blank=True)),
                ('nombre', models.CharField(unique=True, max_length=100)),
                ('slug', models.SlugField(null=True, editable=False, blank=True)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('existencia', models.PositiveIntegerField(null=True, blank=True)),
                ('precioCompra', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('precioVenta', models.DecimalField(max_digits=6, decimal_places=2)),
                ('precioPorMayor', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('imagen', models.ImageField(null=True, upload_to=b'producto', blank=True)),
                ('categoria', models.ForeignKey(to='inventario.Categoria')),
                ('marca', models.ForeignKey(blank=True, to='inventario.Marca', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=100)),
                ('encargado', models.CharField(max_length=100)),
                ('telefono', models.PositiveIntegerField(null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(to='inventario.Proveedor', blank=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
