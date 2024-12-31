# Generated by Django 5.1.4 on 2024-12-30 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[], default='SH', max_length=10),
        ),
    ]