from django.shortcuts import render


menu = [
    {'title':'Главная','url_name':'glavnaya'},
    {'title':'Мудрости','url_name':'mudrosty'},
    {'title':'Вход','url_name':'entrance'},
    # {'title':'Регистрация','url_name':'check_in'},

]


def base(request):
    return render(request, 'base.html', {'menu': menu})

def glavnaya(request):
    return render(request, 'WeZdoms/base.html', {'menu': menu})


def mudrosty(request):
    return render(request, 'WeZdoms/мудрости.html', {'menu': menu})

def entrance(request):
    return render(request, 'WeZdoms/вход.html', {'menu': menu})

# def check_in(request):
#     return render(request, 'WeZdoms/регистрация.html', {'menu': menu})
