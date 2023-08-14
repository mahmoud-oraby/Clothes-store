from rest_framework.permissions import IsAdminUser, SAFE_METHODS

class IsAdminUserOrReadOnly(IsAdminUser):
    """
    Custom permission class that allows read-only access to non-admin users.
    """
    def has_permission(self, request, view):
        is_admin = super(
            IsAdminUserOrReadOnly, 
            self).has_permission(request, view)

        return request.method in SAFE_METHODS or is_admin