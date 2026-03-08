from django.shortcuts import render
from .models import Post

def posts(req):
    posts = Post.objects.all()
    return render(req,'posts.html',{'posts':posts})

def post_details(req,pk):
    post = Post.objects.get(id=pk)
    return render(req,'post_details.html',{'post':post})