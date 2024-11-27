from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Diet, Like


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


class DietAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'value', 'created_at')
    list_filter = ('post', 'user', 'value')
    search_fields = ('user__username', 'post__title')


# Register your models here.
admin.site.register(Comment)
admin.site.register(Diet, DietAdmin)
