

from django.contrib import admin
from .models import Cuisine, Comment
class CuisineAdmin(admin.ModelAdmin):
 list_display = ('name', 'author','created','publish','status')
 
 list_display = ('name', 'author','created','publish','status')
 list_filter = ('status', 'created', 'publish', 'author')
 search_fields = ('name', 'desc')
 prepopulated_fields = {'slug': ('name',)}
 raw_id_fields = ('author',)
 date_hierarchy = 'publish'
 ordering = ['status', 'publish']

admin.site.register(Cuisine, CuisineAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cuisine', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

admin.site.register(Comment, CommentAdmin)
