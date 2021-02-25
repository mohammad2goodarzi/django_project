from django.http import HttpResponse
from django.shortcuts import render

from Main.models import BlogPost


def home_page(request):
    the_title = 'Home'
    qs = BlogPost.objects.all()[:5]
    context = {"title": the_title, "blog_list": qs}
    return render(request, "Home/home.html", context)


def about_page(request):
    the_title = 'About Us'
    return render(request, "Home/about.html", {'title': the_title})


def contact_page(request):
    the_title = 'Contact Us'
    return render(request, "Home/contact.html", {'title': the_title})


def features(request):
    the_title = 'Features'
    return render(request, "Home/feature.html", {'title': the_title})


def preview(request):
    the_title = 'Preview'
    return render(request, "Home/preview.html", {'title': the_title})
