from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    the_title = 'Home'
    the_header = 'Hello, world!!!'
    return render(request, "Home/home.html", {'title': the_title, 'header': the_header})


def about_page(request):
    the_title = 'About Us'
    the_header = 'About Us!!!'
    return render(request, "Home/home.html", {'title': the_title, 'header': the_header})


def contact_page(request):
    the_title = 'Contact Us'
    the_header = 'Contact Us!!!'
    return render(request, "Home/home.html", {'title': the_title, 'header': the_header})


def features(request):
    the_title = 'Features'
    the_header = 'Features!!!'
    return render(request, "Home/home.html", {'title': the_title, 'header': the_header})


def preview(request):
    the_title = 'Preview'
    the_header = 'Preview!!!'
    return render(request, "Home/home.html", {'title': the_title, 'header': the_header})
