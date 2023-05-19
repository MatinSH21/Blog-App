from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'author', 'date_posted']
    search_fields = ['title', 'content']
    list_filter = ['author', 'is_edited']
    inlines = [CommentInline, ]


