from rest_framework.viewsets import ModelViewSet

from apps.character.serializers import UserSerializer, User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
