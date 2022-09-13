from distutils.log import error
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from carsdb.forms import *
from carsdb.models import *

def parts_f(request):
    partsm=parts.objects.all()
    context={
        'partsm':partsm,
    }
    return render(request, 'carsdb/parts.html', context=context)

def cars_f(request):
    carsm=cars.objects.all()
    context={
        'carsm':carsm,
    }
    return render(request, 'carsdb/cars.html', context=context)

def acces_f(request):
    acess = car_part.objects.all()
    context={
        'acess':acess,
    }
    return render(request, 'carsdb/acessor.html', context=context)

def index(request):
    if request.user.is_authenticated:
        return render(request, 'carsdb/index.html')
    else:
        return redirect('login')

class addcars_f(CreateView):
    model = cars
    template_name = 'carsdb/addcars.html'
    success_url = '/cars/'
    form_class = AddCars

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('cars'))


class addparts_f(CreateView):
    model = parts
    template_name = 'carsdb/addparts.html'
    success_url = '/parts/'
    form_class = AddParts

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('parts'))

class register(CreateView):
    form_class = registeruser
    template_name = 'carsdb/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Register'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'carsdb/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Login'
        return context

    def get_success_url(self):
        return reverse_lazy('index')

def logout_user(request):
    logout(request)
    return redirect('login')

