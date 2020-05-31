from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserForm(UserCreationForm):

    superuser = forms.BooleanField(label='superuser')

    class Meta():
        model = User
        fields= ('first_name','last_name','email','username','password1')
    
    def save(self,commit=True):
        user = super(UserForm,self).save(commit=False)
        user.firstname = self.cleaned_data['first_name']
        user.lastname = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.password = self.cleaned_data['password1']
        user.is_superuser = self.cleaned_data['superuser']
        user.is_staff = user.is_superuser

        if commit:
            user.save()
        return user