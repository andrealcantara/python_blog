
from django.contrib import admin
from django.urls import path, include
from .views import blog_hellow, load_index

urlpatterns = [
    path('index_didatico', blog_hellow),
    path('', load_index),
]
