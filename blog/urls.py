from django.urls import path
from .views import show_categories, category_products, product_details


urlpatterns = [
    path('', show_categories, name='show_categories'),
    path('<str:category_slug>', category_products, name='category_products'),
    path('product/<str:product_slug>', product_details, name='product_details'),
]