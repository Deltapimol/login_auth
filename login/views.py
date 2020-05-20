from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def index(request):
    context = { 
                "users" : [1,2,4]
    }
    return render(request,'index.html', context)

def home(request):
    
    return HttpResponse(content=b'Hello! This is home page.')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('index')
        
    else:
        form = UserCreationForm()
    context = { 'form': form }
    return render(request, 'registration/register.html',context)



