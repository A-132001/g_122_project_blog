from django.urls import path
from .views import posts,post_details

urlpatterns = [
    path('posts/',posts,name= "all_posts"),
    path('posts/<int:pk>',post_details,name="post_details")
]