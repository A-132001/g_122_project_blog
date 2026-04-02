from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from .models import Profile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
        
        
class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username',"email","first_name","last_name"]
        
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio","profile_pic","location"]