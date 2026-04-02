from django.urls import path
from .views import login_view,logout_view,register_view,update_user_view
urlpatterns = [
    path("login",login_view,name="login_url"),
    path("logout",logout_view,name="logout_url"),
    path("register",register_view,name="register_url"),
    path("update_user",update_user_view,name="update_user_url"),
    
    

]