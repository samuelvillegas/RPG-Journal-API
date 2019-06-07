from rest_framework.serializers import ModelSerializer, Field

from apps.habittracker.models import Habit, Record


class StreaksField(Field):

    def to_representation(self, obj):
        return obj.calc_streaks()

    def to_internal_value(self, data):
        return data.calc_streaks()


class RecordSerializer(ModelSerializer):

    class Meta:
        model = Record
        fields = '__all__'

    def get_fields(self, *args, **kwargs):
        fields = super(RecordSerializer, self).get_fields(*args, **kwargs)
        request = self.context.get('request', None)
        if request and getattr(request, 'method', None) != "POST":
            fields['habit'].read_only = True
            fields['date'].read_only = True
        return fields


class HabitSerializer(ModelSerializer):
    records = RecordSerializer(many=True, required=False)
    streaks = StreaksField(source='*', required=False)

    class Meta:
        model = Habit
        fields = '__all__'
