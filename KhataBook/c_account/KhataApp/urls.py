from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
path('',views.index,name="index"),
path('new/',views.newcustomer,name="index"),
path('add',views.add,name="index"),
path('tr',views.tr,name="tr"),
path('details/<str:email>',views.details,name="index"),
]