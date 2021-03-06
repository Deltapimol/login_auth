from django.urls import path, include
from . import views

urlpatterns = [

    path('',views.index, name='index'),
    path('home/',views.home, name='home'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('register/',views.register, name='register'),
    path('userform/',views.userform,name='userform'),
    path('customuser/',views.customuser,name='customuser'),
    path('registeruser/',views.registerUser,name='registerUser')
    
]