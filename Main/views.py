from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import BlogPost


def blog_post_details(request, post_id):
    try:
        objects = BlogPost.objects.get(pk=post_id)
    except BlogPost.DoesNotExist:
        raise Http404
    except ValueError:
        raise Http404
    template_name = 'Blog/blog_post.html'
    context = {'object': objects}
    return render(request, template_name, context)
