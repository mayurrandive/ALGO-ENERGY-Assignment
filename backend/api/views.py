from django.shortcuts import render
from rest_framework import views, viewsets, status
from rest_framework.response import Response
from .models import User
from .serializer import UserSerializer
from environ import Env
import requests
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.views import TokenObtainPairView as TRV
from .serializer import MyTokenObtainPairSerializer

from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import check_password

env = Env()
Env.read_env()


class RegisterUser(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # get user data from request body
        user_data = request.data
        # checks
        if not user_data.get('email'):
            return Response({'message': 'email is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not user_data.get('password'):
            return Response({'message': 'password is required'}, status=status.HTTP_400_BAD_REQUEST)
        # create
        user = User.objects.create(
            email=user_data.get('email'),
            password=user_data.get('password'),
            first_name=user_data.get('first_name'),
            last_name=user_data.get('last_name'),
        )
        user.save()
        # hash password
        user.set_password(user.password)
        user.save()
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    

class TokenRefreshView(TRV):
    serializer_class = MyTokenObtainPairSerializer


class SigninView(views.APIView):
    authentication_classes = []  # Set authentication classes to an empty list
    permission_classes = []

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = get_object_or_404(User, email=email)
        except User.DoesNotExist:
            return Response({"errors": ["User not found"]}, status=status.HTTP_404_NOT_FOUND)

        if check_password(password, user.password):
            if not user.is_active:
                return Response({"errors": ["User is not active"]}, status=status.HTTP_400_BAD_REQUEST)

            serializer = MyTokenObtainPairSerializer()
            tokens = serializer.get_token(user)
            user = UserSerializer(user).data
            data = {
                'token': {
                    'access': str(tokens.access_token),
                    'refresh': str(tokens),
                },
                'user': user
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"errors": ["Invalid password"]}, status=status.HTTP_401_UNAUTHORIZED)
