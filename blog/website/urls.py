
from django.contrib import admin
from django.urls import path, include
from .views import blog_hellow, load_index, post_detail

urlpatterns = [
    path('index_didatico', blog_hellow),
    path('', load_index, name="home_url"),
    path('post/<int:id>/', post_detail, name="post_detail"),
]
