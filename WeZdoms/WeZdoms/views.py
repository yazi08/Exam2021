from django.shortcuts import render


menu = [
    {'title':'Главная','url_name':'glavnaya'},
    {'title':'Мудрости','url_name':'mudrosty'},
    {'title':'Вход','url_name':'entrance'},
    {'title':'Регистрация','url_name':'check_in'},

]


def base(request):
    return render(request, 'base.html', {'menu': menu})
