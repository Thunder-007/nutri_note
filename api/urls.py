from django.urls import path, include
from .views import HelloWorld

urlpatterns = [
    path('hello_world/', HelloWorld, name='hello_world'),
]
