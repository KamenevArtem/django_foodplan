from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration.html'
    success_url = reverse_lazy('auth')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'auth.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('lk')


def logout_user(request):
    logout(request)
    return redirect('index')


def index(request):
    return render(request, 'index.html')


def lk(request):
    return render(request, 'lk.html')


def order(request):
    promocode = ''
    if request.method == 'POST':
        print(request.POST)
        promocode = request.POST.get('promocode', '')
        print(promocode)
    return render(request, 'order.html', {'promocode': promocode})


def card(request):
    print(request.POST)
    print(request.POST.get("select1"))
    context = {
        'foodtype': request.POST.get('foodtype'),
        'term': request.POST.get('term'),
        'breakfast': request.POST.get('breakfast'),
        'lunches': request.POST.get('lunches'),
        'dinners': request.POST.get('dinners'),
        'desserts': request.POST.get('desserts'),
        'persons_number': request.POST.get('persons_number'),
        'allergy1': request.POST.get('allergy1'),
        'allergy2': request.POST.get('allergy2'),
        'allergy3': request.POST.get('allergy3'),
        'allergy4': request.POST.get('allergy4'),
        'allergy5': request.POST.get('allergy5'),
        'allergy6': request.POST.get('allergy6'),
    }
    return render(request, 'card.html', context)
    # return render(request, 'order.html', {'bouquet_pk': request.session.get('bouquet_pk', 0)})
