# Generated by Django 5.1.5 on 2025-01-28 06:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_order_details'),
        ('product', '0004_alter_category_description_alter_product_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_details',
        ),
        migrations.AddField(
            model_name='order',
            name='order_details',
            field=models.ManyToManyField(to='product.product'),
        ),
    ]
