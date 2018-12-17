# Generated by Django 2.1.4 on 2018-12-17 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date/Time')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date/Time Modified')),
                ('name', models.CharField(max_length=254, verbose_name='Name')),
                ('mobile', models.CharField(max_length=15, unique=True, verbose_name='Mobile')),
                ('email', models.CharField(max_length=255, unique=True, verbose_name='Email')),
                ('reference', models.TextField(blank=True, null=True, verbose_name='Referer Details')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Lead',
                'verbose_name_plural': 'Leads',
            },
        ),
        migrations.CreateModel(
            name='LeadStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date/Time')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date/Time Modified')),
                ('name', models.CharField(max_length=154, unique=True, verbose_name='Status')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Statuses',
            },
        ),
        migrations.AddField(
            model_name='lead',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lead.LeadStatus', verbose_name='Lead Status'),
        ),
    ]
