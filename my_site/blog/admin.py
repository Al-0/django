from django.contrib import admin

from .models import Tag, Author, Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_filter = ['author', 'tags', 'date']
    list_display = ['title', 'date', 'author']
    prepopulated_fields = {"slug": ("title",)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'post')

# Register your models here.
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
