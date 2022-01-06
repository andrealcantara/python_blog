from django.db import models


class Categories(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(verbose_name='Sub titulo', max_length=200)
    content = models.TextField()
    categorie = models.CharField(
        verbose_name='Categories',
        max_length=2,
        choices=Categories.choices,
        default=Categories.GR,
    )

    def __str__(self):
        return self.title
