from django.contrib import admin

# Register your models here.
from .models import Meal
from .models import MealDay

admin.site.register(Meal)
admin.site.register(MealDay)
