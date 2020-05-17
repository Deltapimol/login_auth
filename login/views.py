from django.shortcuts import render
from django.contrib import auth
from django.forms import forms

def index(request):
    context = { 
                "users" : [1,2,4]
    }
    return render(request,'index.html', context)

