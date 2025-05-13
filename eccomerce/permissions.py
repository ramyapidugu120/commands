from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    message = "You do not have permission to perform this action."

    def has_object_permission(self, request, view, obj):
        # Allow read permissions to anyone.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user.username
