# Generated by Django 2.1.4 on 2019-01-11 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employeedocument_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedocument',
            name='doc_type',
            field=models.CharField(choices=[('P', 'Pan Card'), ('A', 'AADHAR Card'), ('D', 'Driving License'), ('V', 'Voter ID'), ('PEC', 'Previous Employer Certificate'), ('EDU', 'Education Certificate'), ('OFR', 'Offer Letter'), ('NDA', 'Non Disclosure Agreement'), ('PIC', 'Picture')], max_length=5, verbose_name='Document Type'),
        ),
    ]