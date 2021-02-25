from django.contrib import admin
from .models import category,sub_cat,products

# Register your models here.

admin.site.register(category)
admin.site.register(sub_cat)
admin.site.register(products)
