from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateCustomUserForm
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
