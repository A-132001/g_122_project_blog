from django.shortcuts import render
from .models import Post

def posts(req):
    posts = Post.objects.all()
    return render(req,'blog/posts.html',{'posts':posts})

def post_details(req,pk):
    post = Post.objects.get(id=pk)
    comments = post.comments.all()
    return render(req,'blog/post_details.html',{'post':post,"comments":comments})