from django.contrib import admin
from .models import Story
# Register your models here.

class StoryAdmin(admin.ModelAdmin):
    list_display = ['user','created_at']
admin.site.register(Story,StoryAdmin) 