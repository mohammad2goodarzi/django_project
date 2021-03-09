from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category


def show_categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'Blog/categories.html', context)


def category_products(request, category_slug):
    this_category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category=this_category)
    context = {'products': products, 'category': this_category}
    return render(request, 'Blog/category_details.html', context)


def product_details(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {'product': product}
    return render(request, 'Blog/product_details.html', context)
