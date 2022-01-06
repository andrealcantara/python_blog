from django.db import models


class Categories(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(verbose_name='Sub titulo', max_length=200)
    content = models.TextField()
    category = models.CharField(
        max_length=2,
        choices=Categories.choices,
        default=Categories.GR,
        verbose_name='Categorias',
    )
    approved = models.BooleanField(default=True,
                                   verbose_name="Aprovado"
                                   )

    def __str__(self):
        return self.title