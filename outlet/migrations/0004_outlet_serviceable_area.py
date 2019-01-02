# Generated by Django 2.1.4 on 2019-01-02 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20190102_1422'),
        ('outlet', '0003_auto_20190102_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='outlet',
            name='serviceable_area',
            field=models.ManyToManyField(blank=True, to='location.Area', verbose_name='Serviceable Areas'),
        ),
    ]
