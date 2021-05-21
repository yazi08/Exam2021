from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('check_in/', views.register, name = "check_in"),
    path('authorization/', views.LoginUser.as_view(), name = "authorization"),
    path('test/', views.test, name = "test"),
    path('mudrosty/', views.MudrastyView.as_view(), name = "mudrosty"),
]