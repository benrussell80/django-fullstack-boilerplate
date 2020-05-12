import functools

from django.contrib import admin
from .models import Post, Comment

# Register your models here.
def boolean(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    wrapper.boolean = True
    return wrapper


class CommentStackedInline(admin.StackedInline):
    model = Comment
    exclude = ['likes']
    readonly_fields = ['number_of_likes']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [CommentStackedInline]
    exclude = ['likes']
    readonly_fields = ['published', 'number_of_likes']

    @boolean
    def published(self, instance):
        return instance.published


admin.site.register(Comment)