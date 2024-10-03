from django.shortcuts import render,redirect
from .models import Car
from .forms import CarForm

# Create your views here.
def show_cars(request):
    cars = Car.objects.all().order_by("model")
    search = request.GET.get("search")

    if search:# somente verifica se ela não esta vazia
        cars = Car.objects.filter(model__icontains=search)# o underline duplo possibilita a navegação entre tabelas do django
        print(cars)


    context = {
        "cars":cars
    }
    return render(request,'cars.html',context=context)


  
def new_car(request):
    if request.method == "POST":
        new_car_form = CarForm(request.POST,request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()    
            return redirect('cars_list')
            
    else:
        new_car_form = CarForm()
        context = {
            "new_car_form":new_car_form
        }
        return render(request,"new_car.html",context)