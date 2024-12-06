# Create your models here.

from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True)
    poster_url = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return self.title