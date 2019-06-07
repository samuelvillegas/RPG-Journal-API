from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from apps.character.serializers import UserSerializer, User
from apps.habittracker.serializers import HabitSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list_habits(self, request, *args, **kwargs):
        user = self.get_object()

        if user is None:
            raise NotFound

        serializer = HabitSerializer(user.habits.all(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

