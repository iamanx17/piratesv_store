from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class category(models.Model):
    cate=models.CharField(max_length=100,help_text='Enter the category of product')
    
    def __str__(self):
        return self.cate
class sub_cat(models.Model):
    sub_cate=models.CharField(max_length=100, help_text='Enter the sub category of the product')

    def __str__(self):
        return self.sub_cate

class products(models.Model):
    product_name=models.CharField(max_length=150,help_text='Enter the product name')
    desc=models.TextField(help_text='Enter the description of the product')
    price=models.IntegerField(help_text='Enter the price of the product')
    product_img=models.URLField(help_text='Upload the image or enter the url')
    pub_date=models.DateField(auto_now=False, auto_now_add=True)    
    product_cate=models.ForeignKey('category', on_delete=models.CASCADE,help_text='Select the product category')
    product_subcate=models.ForeignKey("sub_cat",on_delete=models.CASCADE,help_text='Select the sub product category')
    user=models.ForeignKey(User,on_delete=models.CASCADE,help_text='Product added by ?')

    def __str__(self):
        return self.product_name