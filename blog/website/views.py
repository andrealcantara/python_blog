from django.shortcuts import render
from .models import Post, Contact


def blog_hellow(request):
    list = ['Django', 'Python', 'Eu', 'tu', 'eles']
    list_posts = Post.objects.all()
    data = {'name': 'Passagem de dicionario no Django',
            'list': list,
            'posts': list_posts}
    return render(request, 'main/index_didatico.html', data)


def load_index(request):
    list_posts = Post.objects.filter(approved=True)
    data = {'posts': list_posts}
    return render(request, 'main/index.html', data)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'main/post.html', {'post': post})


def send_form(request):
    name = request.POST['name']
    Contact.objects.create(name=name,
                           email=request.POST['email'],
                           content=request.POST['message'])
    return render(request, 'main/sucesso.html', {'name': name})
