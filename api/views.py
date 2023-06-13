from django.shortcuts import render, HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from .models import DiveUser
from .serializers import UserSerializer
from .permissions import IsManager


# Create your views here.
def HelloWorld(request):
    return HttpResponse('Hello World')


# views.py


class UserRegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "user created successfully"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)


class UserLoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = DiveUser.objects.filter(username=username).first()
        if user and user.check_password(password):
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key
            })
        return Response({
            'error': 'Invalid credentials'
        }, status=400)


class UserLogoutView(APIView):

    def post(self, request):
        request.user.auth_token.delete()
        return Response({
            'message': 'logout success'
        }, status=200)


class UsersManageView(APIView):
    permission_classes = [IsManager]

    def get(self, request):
        users = DiveUser.objects.filter(level='user')
        user_serializer = UserSerializer(users, many=True)
        return Response({
            'users': user_serializer.data
        }, status=200)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "user created successfully"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)


class UserManageView(APIView):
    permission_classes = [IsManager]

    def get(self, request, pk=None):
        user = DiveUser.objects.get(pk=pk, level='user')
        user_serializer = UserSerializer(user)
        if user_serializer:
            return Response({
                'user': user_serializer.data
            }, status=200)
        return Response({
            'error': 'user not found'
        }, status=400)
