from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf.urls.static import static
urlpatterns = [
    path('', views.index.as_view(), name= 'index'),
    path('home', views.index.as_view(), name = 'home'),
    path('signup/', views.signup.as_view(), name ='signup'),
    path('signin/', views.signin.as_view(), name ='signin'),
    path('signout/', views.signout, name = 'signout')

]
