from django.shortcuts import render
from .models import Car


# Create your views here.
def show_cars(request):
    lista_carros = Car.objects.all().values()
    context = {
        "lista_carros":lista_carros
    }
    return render(request,'cars.html',context=context)
