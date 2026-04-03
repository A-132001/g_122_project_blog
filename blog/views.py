from django.shortcuts import render,redirect
from .models import Post
from .forms import CommentForm,PostForm
from django.contrib.auth.decorators import login_required
def posts(req):
    posts = Post.objects.all()
    return render(req,'blog/posts.html',{'posts':posts})

def post_details(req,pk):
    post = Post.objects.get(id=pk)
    comments = post.comments.all()
    if req.method == "POST":
        form = CommentForm(req.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = req.user.username
            form.save()
            return redirect("post_details",pk=post.id)
    else:
        form = CommentForm()
    context = {'post':post,"comments":comments,'form':form}
    return render(req,'blog/post_details.html',context)

@login_required
def create_post(req):
    if req.method == "POST":
        form = PostForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            return redirect("all_posts")
    else:  
        form = PostForm()
    return render(req,'blog/create_post.html',{"form":form})

def delete_post(req,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect("all_posts")


# apis part
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer

@api_view(['GET','POST'])
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
