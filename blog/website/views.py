from django.shortcuts import render
from .models import Post


def blog_hellow(request):
     list = ['Django', 'Python', 'Eu', 'tu', 'eles']
     list_posts = Post.objects.all();
     data = {'name': 'Passagem de dicionario no Django',
             'list': list,
             'posts': list_posts}
     return render(request, 'index.html', data)


