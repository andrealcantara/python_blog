# Generated by Django 3.2.11 on 2022-01-06 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_post_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categorie',
            field=models.CharField(choices=[('TC', 'Tecnologia'), ('CR', 'Curiosidades'), ('GR', 'Geral')], default='GR', max_length=2, verbose_name='Categories'),
        ),
    ]
