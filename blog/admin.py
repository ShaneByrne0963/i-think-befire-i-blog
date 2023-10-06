from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    # Allows the admin to filter the database items by these keys
    list_filter = ('status', 'created_on')
    # Displays the following keys on the admin database list
    list_display = ('title', 'slug', 'status', 'created_on')
    # Allows the admin to search by title or content
    search_fields = ('title', 'content')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Displays the following keys on the admin database list
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    # Allows the admin to filter the database items by these keys
    list_filter = ('approved', 'created_on')
    # Allows the admin to search by name, body or email
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
