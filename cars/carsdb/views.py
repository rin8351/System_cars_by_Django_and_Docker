from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import CreateView

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
    return render(request, 'carsdb/index.html')

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



