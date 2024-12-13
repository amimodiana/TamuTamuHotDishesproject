from django.urls import path
from .import views


urlpatterns=[
    path('', views.Home, name='home'),
    path('menu/', views.menu, name='menu'),

    path('team/', views.team, name='team'),


]
