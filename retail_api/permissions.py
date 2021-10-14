from rest_framework import permissions

class IsAdminOrReadOnly(permissions.IsAdminUser):
    # for viewing or editing whole list
    def has_permission(self,request, view):
        if request.method in permissions.SAFE_METHODS:
            return True # if GET method
        else:
            return bool(request.user and request.user.is_staff)


class IsReviewer_Staff_ReadOnly(permissions.BasePermission):
    #  single detail obj
    def has_object_permission(self,request, view, object):
        if request.method in permissions.SAFE_METHODS: # if GET
            return True 
        else:
            # allow the actual reviewer OR the admin
            return bool(object.reviewer == request.user or request.user.is_staff)