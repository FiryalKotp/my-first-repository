# Generated by Django 4.1.7 on 2023-04-17 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ArabicName', models.CharField(max_length=80)),
                ('EnglishName', models.CharField(max_length=80)),
                ('code', models.CharField(max_length=80)),
                ('image', models.FileField(blank=True, null=True, upload_to='photo/%y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=50)),
                ('description', models.TextField(blank=True, default='description', max_length=200, null=True)),
                ('code', models.CharField(max_length=80)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='productCategory', to='product.product')),
            ],
        ),
    ]
