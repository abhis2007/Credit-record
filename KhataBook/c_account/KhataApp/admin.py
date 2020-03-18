from django.contrib import admin

# Register your models here.

from .models import new_customer
admin.site.register(new_customer)

from .models import Product_details
admin.site.register(Product_details)

from .models import shop_products
admin.site.register(shop_products)