# Generated by Django 5.0.1 on 2024-02-16 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glamapp', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images/img')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glamapp.product')),
            ],
        ),
    ]
