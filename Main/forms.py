from django import forms
from .models import BlogPost


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['post_title', 'post_content', 'slug']

    # def clean_title(self, *args, **kwargs):
    #     instance = self.instance
    #     title = self.cleaned_data.get('post_title')
    #     qs = BlogPost.objects.filter(post_title__iexact=title)
    #     print(f'... {title} ...')
    #     if instance is not None:
    #         qs = qs.exclude(pk=instance.pk)
    #     if qs.exists():
    #         raise forms.ValidationError("This title has already been used.")
    #     return title
