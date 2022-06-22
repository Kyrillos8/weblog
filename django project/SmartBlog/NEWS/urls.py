from django.urls import path
from . import views


urlpatterns = [
    path('arti/', views.arti, name="arti"), # articels

    ]
