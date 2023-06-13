from django.shortcuts import render, HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from .models import DiveUser
from .serializers import UserSerializer


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


