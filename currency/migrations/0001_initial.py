# Generated by Django 2.1.4 on 2018-12-17 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date/Time')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date/Time Modified')),
                ('name', models.CharField(max_length=254, unique=True, verbose_name='Discount Name')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Discount Value')),
                ('is_percentage', models.BooleanField(default=True, verbose_name='Is Percentage?')),
                ('max_discount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Max Discount Value')),
                ('min_order_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Min Order Amount')),
                ('per_user_limit', models.IntegerField(default=0, verbose_name='Per user limit')),
                ('per_user_value_limit', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Per User Limit (Value)')),
                ('total_count', models.IntegerField(default=0, verbose_name='Total Limit')),
                ('total_value_limit', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Net Value Limit')),
                ('from_date', models.DateField(blank=True, null=True, verbose_name='Valid From (Date)')),
                ('to_date', models.DateField(blank=True, null=True, verbose_name='Valid Till (Date)')),
                ('from_time', models.TimeField(blank=True, null=True, verbose_name='Valid From (Time)')),
                ('to_time', models.TimeField(blank=True, null=True, verbose_name='Valid Till (Time)')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('valid_on_categories', models.ManyToManyField(blank=True, to='product.Category')),
            ],
            options={
                'verbose_name': 'Discount',
                'verbose_name_plural': 'Discounts',
            },
        ),
    ]
