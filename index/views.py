from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import products,category
# Create your views here.

def home(request):
    categ=category.objects.values('cate','id')
    product=[]
    for i in categ:
        pp=products.objects.filter(product_cate=i['id'])
        product.append([i['cate'],pp])
    return render(request,'index.html',{'pro':product})

def viewproduct(request,slug):
    pro=products.objects.filter(product_name=slug)
    cat=products.objects.filter(product_name=slug).values('product_cate')
    for i in cat:
        x=i['product_cate']
    
    recpro=products.objects.filter(product_cate=x).exclude(product_name=slug)  
    return render(request,'product.html',{'pro':pro[0],'recpro':recpro})

def json(request):
    data={
        'Email':'Pran.17am@gmail.com',
        'Username':'iamanx17',
        'Password':'xxxx',

    
    
    
    }
    return JsonResponse(data, safe=False)