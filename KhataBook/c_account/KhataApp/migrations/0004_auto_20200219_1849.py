# Generated by Django 3.0.2 on 2020-02-19 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KhataApp', '0003_product_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_details',
            name='email_id',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='product_details',
            name='product_insert_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 19, 18, 49, 11, 57875)),
        ),
    ]
