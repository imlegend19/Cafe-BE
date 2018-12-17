# Generated by Django 2.1.4 on 2018-12-17 12:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
        ('outlet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date/Time')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date/Time Modified')),
                ('name', models.CharField(blank=True, max_length=254, null=True, verbose_name='Buyer Name')),
                ('mobile', models.CharField(blank=True, max_length=15, null=True, verbose_name='Mobile')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('preparation_time', models.DurationField(default=datetime.timedelta(0, 600), verbose_name='Preparation Time')),
                ('status', models.CharField(choices=[('N', 'New'), ('A', 'Accepted'), ('RJ', 'Rejected'), ('C', 'Cancelled'), ('R', 'Ready'), ('P', 'Picked Up'), ('O', 'Out for Delivery'), ('D', 'Delivered')], default='N', max_length=5, verbose_name='Order Status')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('managed_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='outlet.OutletManager', verbose_name='Outlet Manager')),
                ('outlet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='outlet.Outlet', verbose_name='Outlet')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='SubOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date/Time')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date/Time Modified')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('uom', models.CharField(choices=[('G', 'Grams'), ('KG', 'Kilo Grams'), ('PLT', 'Plates'), ('L', 'Litres'), ('ML', 'Milli Litres'), ('M', 'Meters'), ('KM', 'Kilo Meters'), ('MM', 'Milli Meters'), ('GLS', 'Glasses')], default='PLT', max_length=15, verbose_name='Unit of Measurement')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.Product', verbose_name='Product')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.Order', verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Sub Order',
                'verbose_name_plural': 'Sub Orders',
            },
        ),
    ]
