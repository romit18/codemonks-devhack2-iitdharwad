# Generated by Django 2.2.5 on 2020-01-19 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_maps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maps',
            name='name',
        ),
    ]
