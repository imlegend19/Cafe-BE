# Generated by Django 2.1.4 on 2019-01-01 10:04

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
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date/Time')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date/Time Modified')),
                ('name', models.CharField(max_length=254, unique=True, verbose_name='Tax Name')),
                ('display_name', models.CharField(max_length=254, verbose_name='Bill Display Name')),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Percentage')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tax',
                'verbose_name_plural': 'Taxes',
            },
        ),
    ]
