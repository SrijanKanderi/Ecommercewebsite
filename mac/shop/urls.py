from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name= 'index'),
    path('aboutus/', views.aboutus, name='about us')

]
