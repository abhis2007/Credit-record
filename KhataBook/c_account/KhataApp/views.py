from django.shortcuts import render
from django.http import HttpResponse
from .models import new_customer
from .models import Product_details
from .models import shop_products

def index(request):
    alldata=new_customer.objects.all()

    return render(request,"index.html",{"params":alldata,"l":len(alldata)})

def newcustomer(request):
    return render(request,"Add_Customer.html")

def add(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        c_no=request.POST.get("c_no")
        mail=request.POST.get("email")
    print(first_name,last_name,c_no,mail)
    datas=new_customer(first_name=first_name,last_name=last_name,phone_number=c_no,email_id=mail)
    (Product_details(product_name="testing_shop",product_qty=0.00,product_price=0.00,email_id=mail,total_amount=0.00)).save()
    datas.save()
    return render(request,"Add_Customer.html")

def details(request,email):
    data=Product_details.objects.filter(email_id=email)
    data2=new_customer.objects.filter(email_id=email)
    datas={"params1":data,"params2":data2}
    print(data)
    return render(request, "customer_details.html",datas)

def tr(request):
    p=shop_products.objects.all()
    params1={"param": p}
    return render(request,"try.html",params1)



