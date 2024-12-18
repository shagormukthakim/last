# Generated by Django 5.0.7 on 2024-11-24 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('buy_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('asking_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('selling_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sold_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
