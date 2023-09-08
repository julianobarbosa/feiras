from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """docstring for IsOwnerOrReadOnly.BasePermission"""
    message = 'You must be the owner of this object.'
    my_safe_method = ['GET', 'PUT']

    def has_permission(self, request, view):
        return request.method in self.my_safe_method

    def has_object_permission(self, request, view, obj):
        return True if request.method in SAFE_METHODS else obj.user == request.user
