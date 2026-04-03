from django.urls import path
from .views import posts,post_details,create_post,delete_post,post_list

urlpatterns = [
    path('',posts,name= "all_posts"),
    path('posts/<int:pk>',post_details,name="post_details"),
    path('posts/create',create_post,name="create_post"),
    path('posts/delete/<int:pk>',delete_post,name="delete_post"),

    #apis
    path('apis/posts',post_list,name="post_list"),

]