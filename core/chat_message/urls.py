from django.urls import path
from .views import MessageAPI, GroupAPI

urlpatterns = [
    path('messages/', MessageAPI.as_view(), name='messages-list'), 
    path('messages/user/<str:receiver>/', MessageAPI.as_view(), name='messages-by-user'), 
    path('messages/<int:id>/', MessageAPI.as_view(), name='messages-update-delete'), 
    path('groups/', GroupAPI.as_view(), name='groups-list-create'), 
    path('groups/<str:name>/', GroupAPI.as_view(), name='group-detail'),  
]
