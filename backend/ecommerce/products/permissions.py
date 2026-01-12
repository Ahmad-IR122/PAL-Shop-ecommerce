from rest_framework.permissions import BasePermission

class IsAdminOrSeller(BasePermission):

    def has_permission(self, request, view):
        user = request.user

        if not user or user.is_authenticated:
            return False

        if user.is_staff or user.is_superuser:
            return True

        if user.groups.filter(name='Seller').exists():
            return True

        return False


class IsAdminOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user or user.is_authenticated:
            return False

        if user.is_staff or user.is_superuser:
            return True

        return False