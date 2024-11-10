from django.contrib import admin
from django.urls import  path
from app1.views import Appdev, appdev_reg, cquest, index, register, home, registers, user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register),
    path('index/',index,name='index'),
    path('home/',home),
    path('App/',Appdev,name='App'),
    path('cquest/',cquest),
    path('appdev_reg/',appdev_reg,name='appdev_reg'),
    path('registers/',registers,name='register'),
    path('login/',user_login,name='login'),
]






