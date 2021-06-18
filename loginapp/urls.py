from os import name
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.welcome,name='welcome'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('payment',views.payment,name='payment'),
    #path('image',views.index,name='index')
]
