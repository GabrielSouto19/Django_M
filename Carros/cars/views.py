from django.shortcuts import render,redirect
from .models import Car
from .forms import CarModelForm
from django.views import View

# Create your views here.

class CarsView(View):
    def get(self,request):
        cars = Car.objects.all().order_by("model")
        search = request.GET.get("search")

        if search:# somente verifica se ela não esta vazia
            cars = Car.objects.filter(model__icontains=search)# o underline duplo possibilita a navegação entre tabelas do django
            print(cars)


        context = {
            "cars":cars
        }
        return render(request,'cars.html',context=context)



class NewCarView(View):
    def get(self,request):
        new_car_form = CarModelForm()   
        return render(request,"new_car.html",{"new_car_form":new_car_form})


    def post(self,request):
        new_car_form = CarModelForm(request.POST,request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()    
            return redirect('cars_list')
        return render(request,"new_car.html",{"new_car_form":new_car_form})

