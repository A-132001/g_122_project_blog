from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout

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