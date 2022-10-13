from django.contrib import admin
from .models import BlogPost,Profile,Comment_post

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Comment_post)
admin.site.register(Profile)

