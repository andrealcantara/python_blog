from django.shortcuts import render


def blog_hellow(request):
     lista = ['Django', 'Python', 'Eu', 'tu', 'eles']
     data = {'name': 'Passagem de dicionario no Django', 'lista': lista}
     return render(request, 'index.html', data)


