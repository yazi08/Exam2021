from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import *
from WeZdoms.views import *

from .models import Mudrosty

# class Register(CreateView):
#     form_class = AuthenticationForm
#     template_name = 'register/регистрация.html'
#     context_objects_name = 'form'
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = form
#         return context


def register (request):


    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()



            return redirect('login')
    else:
        form = RegisterUserForm()

    return render(request, "register/регистрация.html", {'form': form,'menu': menu})

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'register/авторизация.html'
    context_objects_name = 'form'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu']=menu
        return context

    def get_success_url(self):
        return reverse_lazy('base')



class MudrastyView(ListView,LoginRequiredMixin):
    paginate_by = 2
    model = Mudrosty
    template_name = "register/мудрости.html"
    context_object_name = 'mudrosty'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu']=menu
        return context

def addmudrosty(request):
    if request.method == 'POST':
        form = AddMudrostyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mudrosty')
    else:
        form = AddMudrostyForm()

    return render(request, "register/Добавить_мудрость.html", {'form':form,'menu':menu} )


# class AddMudrosty(LoginRequiredMixin, DataMixin, CreateView):
#     model = AddMudrostyForm
#     template_name = "register/Добавить_мудрость.html"
#     context_object_name = 'mudrosty_add'
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu']=menu
#         return context

def logout_user(request):
    logout(request)
    return redirect('authorization')