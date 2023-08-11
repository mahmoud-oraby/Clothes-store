# Generated by Django 4.2.3 on 2023-07-25 12:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_remove_product_currency_product_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock_number',
            field=models.PositiveIntegerField(default=10, validators=[django.core.validators.MinValueValidator(10)]),
        ),
    ]
