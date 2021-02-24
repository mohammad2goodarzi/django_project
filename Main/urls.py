from django.urls import path
from .views import blog_post_details, blog_post_list_view, blog_post_delete_view, blog_post_update_view


urlpatterns = [
    path('', blog_post_list_view, name='blog_posts_list'),
    path('<str:slug>', blog_post_details, name='blog_post_details'),
    path('<str:slug>/edit', blog_post_update_view, name='blog_post_edit'),
    path('<str:slug>/delete', blog_post_delete_view, name='blog_post_delete'),
]
