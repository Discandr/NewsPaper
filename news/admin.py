from django.contrib import admin
from .models import Category, Post, PostCategory, Comment, Author


# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(PostCategory)
admin.site.register(Comment)
