# Generated by Django 5.0.1 on 2024-02-16 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glamapp', '0003_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]