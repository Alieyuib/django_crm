# Generated by Django 4.2.3 on 2023-08-10 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_remove_car_manufacturer_remove_car_name_car_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='website.vehicle'),
            preserve_default=False,
        ),
    ]
