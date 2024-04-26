# Generated by Django 5.0.3 on 2024-04-26 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='inventory.product'),
        ),
    ]
