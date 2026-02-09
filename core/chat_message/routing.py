from django.urls import path
from .consumers import *

ws_patterns = [
    path('ws/chat/<str:group_id>', ChatConsumer.as_asgi()),
]