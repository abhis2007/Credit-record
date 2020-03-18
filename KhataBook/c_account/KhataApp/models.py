from django.db import models
from datetime import datetime
# Create your models here.
from django.contrib.auth.models import User

class new_customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone_number=models.IntegerField()
    email_id=models.CharField(max_length=50)

    def __str__(self):
        return self.email_id

class Product_details(models.Model):
    product_name=models.CharField(max_length=50)
    product_qty=models.IntegerField()
    product_price=models.IntegerField()
    total_amount=models.IntegerField()
    email_id = models.CharField(max_length=50,default="")
    product_insert_date=models.DateTimeField(default=datetime.now())

class shop_products(models.Model):
    product_name=models.CharField(max_length=50)
    quantity=models.IntegerField()
    price=models.IntegerField()
    amount=models.IntegerField()

    def __str__(self):
        return self.product_name

