from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name= 'index'),
    path('home', views.index, name = 'home'),
    path('signup/', views.signup, name ='signup')

]
