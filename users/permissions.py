from rest_framework import permissions
from rest_framework.views import View
from users.models import User

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return (request.user.is_superuser or request.method == "GET")
    
class IsAdminOrUser(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return (request.user.is_superuser or request.user == obj)