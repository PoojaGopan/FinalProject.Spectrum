# Generated by Django 5.0.1 on 2024-02-20 10:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glamapp', '0005_contact'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('address', models.TextField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('postcode', models.ImageField(max_length=200, upload_to='')),
                ('phone', models.IntegerField()),
                ('amount', models.CharField(max_length=200)),
                ('payment_id', models.CharField(blank=True, max_length=200, null=True)),
                ('paid', models.BooleanField(default=False, null=True)),
                ('email', models.EmailField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orderitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='pics')),
                ('quantity', models.CharField(max_length=200)),
                ('prize', models.CharField(max_length=200)),
                ('total', models.CharField(max_length=200)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='glamapp.order')),
            ],
        ),
    ]
