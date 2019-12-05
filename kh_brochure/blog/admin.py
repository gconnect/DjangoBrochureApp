from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title']
    # prepopulated_fields = {"slug": ("title",)}
admin.site.register(Blog, BlogAdmin)