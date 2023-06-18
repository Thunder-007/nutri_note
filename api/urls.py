from django.urls import path, include
from .views import HelloWorld, UserRegistrationView, UserLoginView, UserLogoutView, UsersManageView, UserManageView, \
    FoodView, AdminFoodView

urlpatterns = [
    # Hello world endpoint for testing
    path('hello_world/', HelloWorld, name='hello_world'),
    # User registration endpoint only supports user level 'user' use admin panel or shell to create other levels
    path('register/', UserRegistrationView.as_view(), name='register'),
    # User login and logout endpoints
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    # Manager endpoints to manage user data.
    path('manage/users/', UsersManageView.as_view(), name='manage_users'),
    path('manage/users/<int:pk>/', UserManageView.as_view(), name='manage_user'),
    # Individual user endpoints to manage their own food data.
    path('food/', FoodView.as_view(), name='food'),
    # Admin endpoints to manage all food data.
    path('admin/food/', AdminFoodView.as_view(), name='food'),

]
