from django.shortcuts import render
from .models import Post


def blog_hellow(request):
     list = ['Django', 'Python', 'Eu', 'tu', 'eles']
     list_posts = Post.objects.all();
     data = {'name': 'Passagem de dicionario no Django',
             'list': list,
             'posts': list_posts}
     return render(request, 'index.html', data)


def load_index(request):
    list = []
    for i in range(6):
        list.append({'thumb': 'images/thumbs/0' + str(i + 1) + '.jpg',
                     'full': 'images/fulls/0' + str(i+1) + '.jpg'})

    data = {'list_image_post': list}
    return render(request, 'index.html', data)




