from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import BlogPost


def blog_post_details(request, slug):
    # objects = get_object_or_404(BlogPost, slug=slug)
    objects = None
    queryset = BlogPost.objects.filter(slug=slug)
    if queryset.count() >= 1:
        objects = queryset.first()
    template_name = 'Blog/blog_post.html'
    context = {'object': objects}
    return render(request, template_name, context)
