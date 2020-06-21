from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField
    status = models.CharField(max_length=10, choices=[('D', 'draft'), ('P', 'published')])
    content = models.TextField()
    updated = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(default=timezone.now)
    # category = models.ForeignKey('Category', on_delete=models.CASCADE, default=None)
    category = models.ForeignKey('Category', related_name='category',
                                 null=True,
                                 blank=True,
                                 verbose_name='Категория',
                                 on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=' Название категории')
    url = models.SlugField(max_length=255, db_index=True)

    def __str__(self):
        return self.name
