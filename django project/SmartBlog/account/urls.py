from django.urls import path
from . import views

app_name = "main"   

urlpatterns = [
    path('register', views.register, name="register"), # signUp
    path('login/', views.login_request, name="login"), # LOgin
    path('logout', views.logout_user, name="logout"), # signout
    path('profile', views.profile, name="profile"), # profile


    #path('signup', views.signup, name="signup"), # signUp


    ]



