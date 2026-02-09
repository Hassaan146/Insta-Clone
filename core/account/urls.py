from django.urls import path
from .views import RegisterAPI,LoginAPI,LogoutAPI,ProfileAPI

urlpatterns = [
    path('register/',RegisterAPI.as_view(), name="register"),
    path('login/' , LoginAPI.as_view() , name="login"),
    path('logout/' , LogoutAPI.as_view() , name="login_out"),
    path('profile/' , ProfileAPI.as_view() , name="profile_create"),
    path('profile/<int:id>' , ProfileAPI.as_view() , name="profile_get"),
]
