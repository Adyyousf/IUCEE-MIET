# Generated by Django 3.2.5 on 2021-08-09 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_date_mom_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mom',
            name='time',
            field=models.DateField(),
        ),
    ]
