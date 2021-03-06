# Generated by Django 2.1.4 on 2019-01-15 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_orderpayment_accepted_by'),
        ('currency', '0002_ocpointtransaction_ocpointwallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='ocpointtransaction',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='transaction.OrderPayment', verbose_name='Order Payment'),
        ),
    ]
