# Generated by Django 4.2.3 on 2023-09-22 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_cartorder_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='price',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
