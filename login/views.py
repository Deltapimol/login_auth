from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django import forms
from login import forms as forms_py

class CustomForm(UserCreationForm):

    firstname = forms.CharField(label='firstname')
    lastname = forms.CharField(label='lastname')
    email = forms.EmailField(label='email')   

    class Meta:
        model=User
        fields = ('firstname','lastname','email','username') # <- This actually creates the fields in form
        
    def save(self,commit=True):
        user = super(CustomForm,self).save(commit=False)
        user.firstname = self.cleaned_data['firstname']
        user.lastname = self.cleaned_data['lastname']
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.password = self.cleaned_data['password1']
        if commit:
            user.save()
        return user

def registerUser(request):
    if request.method == 'POST':
        form = forms_py.UserForm(request.POST)
        if form.is_valid():
            user = form.save()

            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()

            login(request,user)
            return redirect('index')
    else:
        form = forms_py.UserForm()
    context = { 'form': form }
    return render(request,'registration/registeruser.html',context)

def userform(request):
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #user = authenticate(username=username,password=password)
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
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







    




