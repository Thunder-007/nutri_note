from django.urls import path, include
from .views import HelloWorld, UserRegistrationView, UserLoginView, UserLogoutView, UsersManageView, UserManageView

urlpatterns = [
    path('hello_world/', HelloWorld, name='hello_world'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('manage/users/', UsersManageView.as_view(), name='manage_users'),
    path('manage/users/<int:pk>/', UserManageView.as_view(), name='manage_user'),
]
