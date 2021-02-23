from django.db import models


class BlogPost(models.Model):
    post_title = models.CharField(max_length=200)
    post_content = models.TextField(null=True, blank=True)
    slug = models.SlugField(default="")


