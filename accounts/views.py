from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm



def login_view(request,*args,**kwargs):
    return render(request)



def logout_view(request,*args, **kwargs):
    return render(request)



def register_view(request,*args, **kwargs):
    return render(request)

