# Generated by Django 5.1.4 on 2025-01-17 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0009_alter_products_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="Image",
            field=models.URLField(max_length=500),
        ),
    ]
