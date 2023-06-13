from rest_framework import permissions


class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.level == 'moderator' or request.user.level == 'admin'
