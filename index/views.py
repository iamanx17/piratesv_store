from django.shortcuts import render
from .models import products,category
# Create your views here.

def home(request):
    pro=products.objects.all()
    categ=category.objects.values('cate','id')
    product=[]
    for i in categ:
        pp=products.objects.filter(product_cate=i['id'])
        product.append([i['cate'],pp])
    return render(request,'index.html',{'pro':product})