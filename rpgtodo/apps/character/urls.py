from django.urls import path

from apps.character.views import UserViewSet

urlpatterns = [
    path('users/', UserViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('users/<int:pk>/', UserViewSet.as_view({
        'get': 'retrieve',
        'post': 'update',
        'delete': 'destroy',
    })),
]
