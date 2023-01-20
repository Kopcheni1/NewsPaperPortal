from django.contrib import admin
from .models import Post, Category, PostCategory


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'categoryType', 'rating')
    list_filter = ('author', 'categoryType', 'rating')
    search_fields = ('rating', 'title')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(PostCategory)

