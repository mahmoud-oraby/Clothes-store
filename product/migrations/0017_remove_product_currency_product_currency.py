# Generated by Django 4.2.3 on 2023-07-24 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_alter_product_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='currency',
        ),
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.ManyToManyField(to='product.currency'),
        ),
    ]
