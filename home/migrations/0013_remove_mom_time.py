# Generated by Django 3.2.5 on 2021-08-09 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_mom_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mom',
            name='time',
        ),
    ]
