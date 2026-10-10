from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    message = 'Admin access required.'
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'admin')

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.method in ('GET','HEAD','OPTIONS'):
            return True
        return request.user.role == 'admin'
