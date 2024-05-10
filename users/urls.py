from django.urls import path, include
from users.views import UserAuthorizationAPIView, RegisterUserAPIView, UserViewSet

urlpatterns = [
    path("authorization/", UserAuthorizationAPIView.as_view(), name="user-authorization"),
    path('register/', RegisterUserAPIView.as_view(), name='register_user'),

]