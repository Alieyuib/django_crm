# Generated by Django 4.2.3 on 2023-08-10 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_car_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vin',
            field=models.CharField(max_length=100),
        ),
    ]
