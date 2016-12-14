import services
from recipes.models import Meal, MealDay
from recipes.serializers import MealSerializer, MealDaySerializer, PinSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response


class PinList(APIView):
    def get(self, request, format=None):
        pins = services.get_pins()
        serializer = PinSerializer(pins, many=True)
        return Response(serializer.data)


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class MealDayViewSet(viewsets.ModelViewSet):
    queryset = MealDay.objects.all()
    serializer_class = MealDaySerializer
