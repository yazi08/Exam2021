from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('check_in/', views.register, name = "check_in"),
    path('logout/', views.logout_user, name = "logout"),
    path('authorization/', views.LoginUser.as_view(), name = "authorization"),
    path('mudrosty/', views.MudrastyView.as_view(), name = "mudrosty"),
    path('mudrosty_add/', views.addmudrosty, name = "mudrosty_add"),
    path('<int:pk>/delete', views.MudrastyDelete.as_view(), name = "delete"),
]