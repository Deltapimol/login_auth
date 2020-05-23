from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django import forms

class CustomForm(UserCreationForm):

    firstname = forms.CharField(label='First name')
    lastname = forms.CharField(label='Last name')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ('firstname','lastname','email')
    
    def save(self,commit=True):
        user = super(CustomForm,self).save(commit=False)
        user.firstname = self.cleaned_data['firstname']
        user.lastname = self.cleaned_data['lastname']
        user.email = self.cleaned_data['email']
        user.password = self.cleaned_data['password']
        if commit:
            user.save()
        return user

def userform(request):
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            form.save()
            name1 = form.cleaned_data['firstname']
            name2 = form.cleaned_data['lastname'] 
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email,password=password)
            login(request,user)
            return redirect('customuser')
    else:
        form = CustomForm()
    context = { 'form': form }
    return render(request,'registration/userform.html',context)

def customuser(request):
    context = {'user' : request.user}
    return render(request,'registration/customuser.html',context)
            
def index(request):
    return render(request,'index.html')

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







    




