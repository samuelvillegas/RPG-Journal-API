from django.urls import path

from apps.character.views import UserViewSet

urlpatterns = [
    path('users/', UserViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('user/<int:pk>/', UserViewSet.as_view({
        'get': 'retrieve',
        'post': 'update',
        'delete': 'destroy',
    })),
    path('user/<int:pk>/habits/', UserViewSet.as_view({
        'get': 'list_habits'
    }))
]
