from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.
def register_user(request):
    if request.method == "POST":
        user_form  = UserCreationForm(request.POST)
        
        if user_form.is_valid():
            user_form.save()
            print("Cheguei ate aqui 3")
            return redirect('cars_list')
    else:
        
        user_form  = UserCreationForm()  
    
    return render(request,'register.html',{'user_form':user_form})

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            print(f"Estou chegando ate aqui{user}")
            login(request,user)
            return redirect("new_car")
        else:
            auth_form = AuthenticationForm()



    else:
        auth_form = AuthenticationForm()
    return render(request,'login.html',{'auth_form':auth_form})