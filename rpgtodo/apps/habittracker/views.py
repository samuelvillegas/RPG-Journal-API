from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from apps.habittracker.serializers import HabitSerializer, Habit, RecordSerializer, Record


class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class RecordViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
