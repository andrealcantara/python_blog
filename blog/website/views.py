from django.shortcuts import render
from django.http import request, HttpResponse


# Create your views here.


def blog_hellow(request):
    return HttpResponse("Blog");

