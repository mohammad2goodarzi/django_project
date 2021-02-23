from django.http import HttpResponse
from django.shortcuts import render

from .models import BlogPost


def blog_post_details(request):
    objects = BlogPost.objects.get(pk=2)
    template_name = 'Blog/blog_post.html'
    context = {'object': objects}
    return render(request, template_name, context)
