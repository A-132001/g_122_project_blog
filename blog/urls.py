from django.urls import path
from .views import posts,post_details

urlpatterns = [
    path('posts/',posts),
    path('posts/<int:pk>',post_details)
]