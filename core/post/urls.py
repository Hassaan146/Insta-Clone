from django.urls import path
from .views import *


urlpatterns = [
    path('comments/<int:id>' , CommentAPI.as_view(),name="comments"),
    path('comments/' , CommentAPI.as_view(),name="comments_write"),
    path('post/',PostAPI.as_view() ,name="posts_create"),
    path('post/<int:id>',PostAPI.as_view() ,name="posts"),
]
