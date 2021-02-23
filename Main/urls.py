from django.urls import path
from .views import blog_post_details


urlpatterns = [
    path('<str:slug>', blog_post_details, name='blog_post_details'),
]
