from django.urls import path, include
from .views import HelloWorld, UserRegistrationView

urlpatterns = [
    path('hello_world/', HelloWorld, name='hello_world'),
    path('register/', UserRegistrationView.as_view(), name='register'),
]
