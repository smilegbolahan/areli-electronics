# Generated by Django 4.2.3 on 2023-09-22 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_cartorder_paid_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartorder',
            name='price',
        ),
        migrations.RemoveField(
            model_name='cartorder',
            name='product_status',
        ),
    ]
