# Generated by Django 5.1.4 on 2025-01-02 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Category',
            field=models.CharField(choices=[('select', 'Select'), ('dog', 'Dog'), ('cat', 'Cat')], default='select', max_length=6),
        ),
    ]