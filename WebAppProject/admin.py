from django.contrib import admin
from WebAppProject.models import Category, Post, Comment
from WebAppProject.models import UserProfile

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile)
