from django.urls import path
from .views import blog_post_details


urlpatterns = [
    path('<int:post_id>', blog_post_details, name='blog_post_details'),
]
