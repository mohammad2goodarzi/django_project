from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import BlogPost
from .forms import BlogPostModelForm


def blog_post_details(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    # objects = None
    # queryset = BlogPost.objects.filter(slug=slug)
    # if queryset.count() >= 1:
    #     objects = queryset.first()
    template_name = 'Blog/detail.html'
    context = {'object': obj}
    return render(request, template_name, context)


def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    template_name = 'Blog/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)


@login_required
# @staff_member_required
def blog_post_create_view(request):
    # create objects
    # ? use a form
    if request.method == "POST":
        form = BlogPostModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('blog_posts_list')
    else:
        form = BlogPostModelForm()
        template_name = 'Blog/form.html'
        context = {'form': form}
        return render(request, template_name, context)


def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'Blog/update.html'
    context = {"object": obj, 'form': None}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'Blog/delete.html'
    context = {"object": obj}
    return render(request, template_name, context)
