
from django.contrib import admin
from django.urls import path, include
from .views import blog_hellow

urlpatterns = [
    path('', blog_hellow),
]