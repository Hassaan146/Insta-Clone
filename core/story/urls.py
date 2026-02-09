from django.urls import path
from .views import StoryAPI

urlpatterns = [
    path('stories/', StoryAPI.as_view(), name='story-list-create'),
    path('stories/<int:id>/', StoryAPI.as_view(), name='story-detail'),
]
