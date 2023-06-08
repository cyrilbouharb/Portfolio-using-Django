# CREATED THIS FILE FROM SCRATCH
from django.urls import path
from . import views



urlpatterns = [
    path('', views.allblogs, name='allblogs')
] 
