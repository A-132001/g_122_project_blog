from django.shortcuts import render
from .models import Post

def posts(req):
    posts = Post.objects.all()
    return render(req,'posts.html',{'posts':posts})