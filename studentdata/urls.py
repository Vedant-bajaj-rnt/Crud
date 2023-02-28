from django.contrib import admin
from django.urls import path,include
from Studentdata import views

urlpatterns = [
    path('',views.Home),
    path('send',views.send),
    path('delete',views.delete),
    path('Home',views.Home),
    path('edit',views.edit)
    
]