from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('check_in/', views.check_in, name = "check_in"),
]