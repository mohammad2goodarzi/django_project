from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, "Home/home.html")


def about_page(request):
    return HttpResponse("<h1>About Us</h1>")


def contact_page(request):
    return HttpResponse("<h1>Contact Us</h1>")


def features(request):
    return HttpResponse("<h1>Features</h1>")


def preview(request):
    return HttpResponse("<h1>Preview</h1>")
