# Generated by Django 3.2.5 on 2021-08-09 15:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_mom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
