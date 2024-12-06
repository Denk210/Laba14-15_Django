# Create your models here.

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255, default='Denis')

    class Meta:
        verbose_name_plural = "Авторы"

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True)
    poster_url = models.URLField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='films', default="1")

    class Meta:
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return self.title