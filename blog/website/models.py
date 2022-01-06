from django.db import models


class Categories(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    sub_title = models.CharField(verbose_name='Sub titulo', max_length=200)
    content = models.TextField(verbose_name="Conteudo")
    category = models.CharField(
        max_length=2,
        choices=Categories.choices,
        default=Categories.GR,
        verbose_name='Categorias',
    )
    approved = models.BooleanField(default=True,
                                   verbose_name="Aprovado"
                                   )

    image_post = models.ImageField(upload_to="posts", null=True, blank=True, verbose_name="Imagem")

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nome")
    email = models.EmailField()
    content = models.TextField(verbose_name="Conteudo")