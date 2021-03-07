from django.contrib import admin
from .models import BlogPost


admin.site.site_header = 'The_project Admin'
admin.site.index_title = 'Main Admin'
admin.site.site_title = 'django'

admin.site.register(BlogPost)
