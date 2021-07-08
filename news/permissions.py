from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsNewsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsCommentOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'DELETE':
            return obj.owner == request.user or obj.news.owner == request.user
        return obj.owner == request.user
