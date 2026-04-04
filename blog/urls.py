from django.urls import path,include
from .views import PostViewset,CommentViewset,posts,post_details,create_post,delete_post,post_list,post_detail_api
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('viewsets/posts',PostViewset)
router.register('viewsets/comments',CommentViewset)



urlpatterns = [
    path('',posts,name= "all_posts"),
    path('posts/<int:pk>',post_details,name="post_details"),
    path('posts/create',create_post,name="create_post"),
    path('posts/delete/<int:pk>',delete_post,name="delete_post"),
    #viewset
    path('apis/',include(router.urls)),
    #apis
    path('apis/posts',post_list,name="post_list"),
    path('apis/posts/<int:pk>',post_detail_api,name="post_detail"),

]