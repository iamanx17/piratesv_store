from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<str:slug>',views.viewproduct,name='viewproduct'),
    path('json',views.json,name='json')
]
