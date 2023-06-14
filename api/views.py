from django.shortcuts import render, HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from .models import DiveUser
from .serializers import UserSerializer
from .permissions import IsManager
from rest_framework.generics import CreateAPIView


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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        }, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):

    def post(self, request):
        request.user.auth_token.delete()
        return Response({
            'message': 'logout success'
        }, status=status.HTTP_400_BAD_REQUEST)


class UsersManageView(APIView):
    permission_classes = [IsManager]

    def get(self, request):
        users = DiveUser.objects.filter(level='user')
        user_serializer = UserSerializer(users, many=True)
        return Response({
            'users': user_serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "user created successfully"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserManageView(CreateAPIView):
    permission_classes = [IsManager]
    serializer_class = UserSerializer

    def get(self, request, pk=None):
        try:
            user = DiveUser.objects.get(pk=pk, level='user')
        except DiveUser.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            user = DiveUser.objects.get(pk=pk)
        except DiveUser.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        try:
            user = DiveUser.objects.get(pk=pk, level='user')
        except DiveUser.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user = DiveUser.objects.get(pk=pk, level='user')
        except DiveUser.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
