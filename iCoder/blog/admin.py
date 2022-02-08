from django.contrib import admin
from .models import Post
from blog.models import Post, BlogComment


admin.site.register((Post, BlogComment))