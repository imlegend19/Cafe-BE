# Generated by Django 2.1.4 on 2018-12-17 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date/Time')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date/Time Modified')),
                ('name', models.CharField(max_length=254, unique=True, verbose_name='Business Name')),
                ('business_type', models.CharField(choices=[('I', 'Individual/Proprietorship'), ('PL', 'Private Limited'), ('L', 'Limited (Public Company)'), ('LLP', 'Limited Liability Partnership (LLP)'), ('P', 'Partnership')], default='PL', max_length=5, verbose_name='Business Type')),
                ('gst', models.CharField(blank=True, max_length=15, null=True, verbose_name='GST Number')),
                ('pan', models.CharField(max_length=10, unique=True, verbose_name='PAN Number')),
                ('fssai', models.CharField(blank=True, max_length=150, null=True, verbose_name='FSSAI License Number')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active?')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('managers', models.ManyToManyField(blank=True, related_name='manages_businesses', to=settings.AUTH_USER_MODEL, verbose_name='Managers')),
                ('owners', models.ManyToManyField(blank=True, related_name='owns_businesses', to=settings.AUTH_USER_MODEL, verbose_name='Owners')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='location.State', verbose_name='Home State')),
            ],
            options={
                'verbose_name': 'Business',
                'verbose_name_plural': 'Businesses',
            },
        ),
        migrations.CreateModel(
            name='BusinessDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date/Time')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date/Time Modified')),
                ('doc_type', models.CharField(choices=[('F', 'FSSAI License'), ('P', 'Pan Card'), ('A', 'AADHAR Card'), ('COI', 'Certificate of Incorporation'), ('T', 'TAN Card'), ('G', 'GST Registration'), ('MOA', 'Memorandum of Association'), ('AOA', 'Agreement of Association'), ('RA', 'Rental Agreement')], max_length=5, verbose_name='Document Type')),
                ('value', models.CharField(blank=True, max_length=254, null=True, verbose_name='Doc Value')),
                ('status', models.CharField(choices=[('F', 'Verification Failed'), ('P', 'Pending Verification'), ('V', 'Verified')], default='P', max_length=5, verbose_name='Verification Status')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='business.Business', verbose_name='Business')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Business Document',
                'verbose_name_plural': 'Business Documents',
            },
        ),
    ]
