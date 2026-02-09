from django.contrib import admin
from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['user','description','created_at']
admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','text','created_at']
admin.site.register(Comments,CommentAdmin)

class FeedAdmin(admin.ModelAdmin):
    list_display = ['user']
admin.site.register(Feed,FeedAdmin)