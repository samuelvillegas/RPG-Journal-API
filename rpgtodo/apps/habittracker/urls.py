from django.urls import path

from apps.habittracker.views import HabitViewSet, RecordViewSet

urlpatterns = [
    path('habits/', HabitViewSet.as_view({
        'post': 'create',
    })),
    path('records/', RecordViewSet.as_view({
        'post': 'create',
    })),
    path('record/<int:pk>/', RecordViewSet.as_view({
        'delete': 'destroy',
        'put': 'update'
    }))
]
