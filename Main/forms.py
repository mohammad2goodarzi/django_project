from django import forms
from .models import BlogPost



class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['post_title', 'post_content', 'slug']

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('post_title')
        print(title)
        qs = BlogPost.oblects.filter(post_title__iexact=title)
        if qs.exists():
            raise forms.ValidationError("This title has already been used.")
        return title
