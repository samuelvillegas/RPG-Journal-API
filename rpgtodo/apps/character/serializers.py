from rest_framework.serializers import ModelSerializer

from apps.character.models import User, Skill, Character


class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class CharacterSerializer(ModelSerializer):
    class Meta:
        model = Character
        exclude = ('user',)


class UserSerializer(ModelSerializer):
    character = CharacterSerializer(many=False)
    skills = SkillSerializer(many=True)

    class Meta:
        model = User
        exclude = ('groups', 'password', 'is_superuser', 'is_staff', 'user_permissions', 'date_joined')

