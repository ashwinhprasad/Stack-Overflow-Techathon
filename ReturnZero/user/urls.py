from django.urls import path, include
from .views import UserSignup, UserSignin

urlpatterns = [
    path('signup/',UserSignup,name='signup'),
    path('signin/',UserSignin,name='signin')
]
