from django.shortcuts import render
from django.contrib import auth
from django.forms import forms
from django.http import HttpResponse

def index(request):
    context = { 
                "users" : [1,2,4]
    }
    return render(request,'index.html', context)

def home(request):
    
    return HttpResponse(content=b'Hello! This is home page.')