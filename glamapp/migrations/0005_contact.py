# Generated by Django 5.0.1 on 2024-02-19 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glamapp', '0004_alter_images_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
    ]
