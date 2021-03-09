from django.db import models
from django.db.models import *


class Category(models.Model):
    title = CharField(max_length=200)
    slug = SlugField(default='', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/category/{self.slug}'


class Product(models.Model):
    category = ForeignKey(Category, on_delete=PROTECT)
    image = ImageField(upload_to='product_image/')
    title = CharField(max_length=200)
    slug = SlugField(default='', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/category/product/{self.slug}'
