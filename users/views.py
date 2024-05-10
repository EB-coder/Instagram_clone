# users/views.py

from rest_framework import viewsets
from .models import UserProfile, User
from .serializers import UserProfileSerializer, AuthorizationUserSerializer, RegisterUserSerializer, UserSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserAuthorizationAPIView(generics.CreateAPIView):
    serializer_class = AuthorizationUserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data["username"]
        password = request.data["password"]
        user = User.objects.filter(username=username, password=password)
        if user:
                return Response({
                    'status': "success",
                    'id': user[0].id,
                }, status.HTTP_200_OK)
        return Response({
                    'status': "error"
                }, status=status.HTTP_400_BAD_REQUEST)


class RegisterUserAPIView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer

     