from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL


class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    post_title = models.CharField(max_length=200)
    post_content = models.TextField(null=True, blank=True)
    slug = models.SlugField(default="", unique=True)


