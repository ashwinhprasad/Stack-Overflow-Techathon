from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateCustomUserForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def UserSignup(request):
    signup_form = CreateCustomUserForm()
    if request.method == "POST":
        signup_form = CreateCustomUserForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return HttpResponse("User Created")
        else:
            print("not valid")
    else:
        print("method is not post")
    return render(request,'user/signup.html',{"form":signup_form})


def UserSignin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return HttpResponse("Login Success")
        else:
            return HttpResponse("User Does not Exist")
    return render(request,'user/signin.html',{})
