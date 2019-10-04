from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

admin.site.register(Blog, BlogAdmin)