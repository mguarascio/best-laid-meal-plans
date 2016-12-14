from django.conf.urls import url, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'meals', views.MealViewSet)
router.register(r'mealdays', views.MealDayViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^pin-list/', views.PinList.as_view())
]
