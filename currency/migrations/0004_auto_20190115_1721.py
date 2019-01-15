# Generated by Django 2.1.4 on 2019-01-15 11:51

from django.db import migrations


def create_wallet(apps, schema_editor):
    from django.contrib.auth import get_user_model

    User = get_user_model()

    WalletModel = apps.get_model('currency', 'OCPointWallet')

    users = User.objects.all()

    for user in users:
        WalletModel.objects.get_or_create(created_by_id=user.id)


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_ocpointtransaction_payment'),
    ]

    operations = [
        migrations.RunPython(create_wallet),
    ]
