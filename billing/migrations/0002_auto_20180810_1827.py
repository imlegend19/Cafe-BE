# Generated by Django 2.0.7 on 2018-08-10 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('billing', '0001_initial'),
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='billitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurant.Item'),
        ),
        migrations.AddField(
            model_name='billingheader',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='billingheader',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurant.Store'),
        ),
    ]