from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView

menu = [
    {'title':'Главная','url_name':'glavnaya'},
    # {'title':'Мудрости','url_name':'mudrosty'},
    #{'title':'Вход','url_name':'entrance'},
    #{'title':'Регистрация','url_name':'register'},
    # {'title':'Регистрация','url_name':'check_in'},

]



def base(request):
    obj = User.objects.all()
    return render(request, 'base.html', {'menu': menu,'obj':obj})

def glavnaya(request):

    return render(request, 'base.html', {'menu': menu})



def entrance(request):
    return render(request, 'WeZdoms/вход.html', {'menu': menu})

# def check_in(request):
#     return render(request, 'WeZdoms/регистрация.html', {'menu': menu})


def login(request):
    return render(request, "register/успешная регистрация.html")

