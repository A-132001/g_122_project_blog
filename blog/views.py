from django.shortcuts import render,redirect
from .models import Post,Comment
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
from rest_framework import status,viewsets,permissions
from .serializers import PostSerializer,CommentSerializer


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    
class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]
    


@api_view(['GET','POST'])
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = PostSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
@api_view(["GET","PUT","PATCH","DELETE"])
def post_detail_api(request,pk):
    try:
        post = Post.objects.get(id=pk)
    except:
        return Response({"error":"post not found"},status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data,status=status.HTTP_200_OK)
    # Update full
    elif request.method == "PUT":
        serializer = PostSerializer(post,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        
    elif request.method == "PATCH":
        serializer = PostSerializer(post,data= request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        
    elif request.method == "DELETE":
        post.delete()
        return Response({"message":"Post Deleted"},status=status.HTTP_204_NO_CONTENT)