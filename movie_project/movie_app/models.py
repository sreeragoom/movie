from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('movie_app:movies_by_category', args=[self.slug])


class Movies(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    poster = models.ImageField(upload_to="poster_pic")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    year = models.DateField()
    description = models.TextField(max_length=700)
    actors = models.TextField()
    links = models.TextField()

    class Meta:
        ordering = ('title',)
        verbose_name = 'movies'
        verbose_name_plural = 'moviess'

    def __str__(self):
        return '{}'.format(self.title)

    def get_url(self):
        return reverse('movie_app:detail', args=[self.category.slug, self.slug])
