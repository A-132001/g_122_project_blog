from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from .forms import RegisterForm,UpdateProfileForm,UpdateUserForm
def login_view(req):
    if req.method == "POST":
        form = AuthenticationForm(data = req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req,user)
            return redirect("all_posts")
    else:
        form = AuthenticationForm()
    
    return render(req,'accounts/login.html',{"form":form})


def logout_view(req):
    logout(req)
    return redirect("all_posts")

def register_view(req):
    if req.method == "POST":
        form = RegisterForm(data = req.POST)
        if form.is_valid():
            user = form.save()
            login(req,user)
            return redirect("all_posts")
    else:
        form = RegisterForm()
    return render(req,'accounts/register.html',{"form":form})
    
    
def update_user_view(req):
    if req.method == "POST":
        user_form = UpdateUserForm(req.POST,instance=req.user)
        profile_form = UpdateProfileForm(req.POST,req.FILES,instance=req.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("update_user_url")
    else:
        user_form = UpdateUserForm(instance=req.user)
        profile_form = UpdateProfileForm(instance=req.user.profile)
    
    return render(req,"accounts/update_user.html",{"user_form":user_form,"profile_form":profile_form})