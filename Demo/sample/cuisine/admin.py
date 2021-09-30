

from django.contrib import admin
from .models import Cuisine
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
