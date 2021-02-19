from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    the_title = 'Home'
    return render(request, "Home/home.html", {'title': the_title})


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
