from django.db import models


class BlogPost(models.Model):
    post_title = models.TextField()
    post_content = models.TextField(null=True, blank=True)
