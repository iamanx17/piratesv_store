from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
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

def viewproduct(request,id):
    pro=products.objects.filter(id=id)
    recpro=products.objects.filter(product_cate=id).exclude(id=id)
    print(recpro)

    return render(request,'product.html',{'pro':pro[0],'recpro':recpro})

def json(request):
    data={
        'Email':'Pran.17am@gmail.com',
        'Username':'iamanx17',
        'Password':'xxxx',

    
    
    
    }
    return JsonResponse(data, safe=False)