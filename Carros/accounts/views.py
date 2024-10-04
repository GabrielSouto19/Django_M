from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.
def register_user(request):
    if request.method == "POST":
        user_form  = UserCreationForm(request.POST)
        
        if user_form.is_valid():
            user_form.save()
            print("Cheguei ate aqui 3")
            return redirect('login')
    else:
        
        user_form  = UserCreationForm()  
    
    return render(request,'register.html',{'user_form':user_form})

def login_view(request):
    # login do djangoteste é ingh123456
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            print(f"Estou chegando ate aqui{user}")
            login(request,user)
            return redirect("cars_list")
        else:
            auth_form = AuthenticationForm()



    else:
        auth_form = AuthenticationForm()
    return render(request,'login.html',{'auth_form':auth_form})

def logout_view(request):
    logout(request)
    return redirect("cars_list")