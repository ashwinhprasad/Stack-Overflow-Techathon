from django.urls import path, include
from .views import UserSignup

urlpatterns = [
    path('signup/',UserSignup,name='signup')
]
