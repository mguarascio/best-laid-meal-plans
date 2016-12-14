from recipes.models import Pin, Meal, MealDay
from rest_framework import serializers


class PinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pin
        fields = ('id', 'url', 'note', 'image', 'title')


class MealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meal
        fields = ('url', 'image', 'title')


class MealDaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MealDay
        fields = (['meal_day'])
