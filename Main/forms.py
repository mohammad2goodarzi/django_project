from django import forms
from .models import BlogPost


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['post_title', 'post_content', 'slug']
