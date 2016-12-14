from recipes.models import Pin, Meal, MealDay
from rest_framework import serializers


class PinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pin
        fields = ('id', 'url', 'note', 'image', 'title')


class MealDaySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MealDay
        fields = (['date'])


class MealSerializer(serializers.HyperlinkedModelSerializer):
    meal_day = MealDaySerializer()

    class Meta:
        model = Meal
        fields = ('url', 'image', 'title', 'meal_day')
