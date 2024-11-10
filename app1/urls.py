from django.contrib import admin
from django.urls import path

from app1.views import Appdev, cquest, index, register, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register),
    path('index/',index),
    path('home/',home),
    path('App/',Appdev),
    path('cquest/',cquest),
]