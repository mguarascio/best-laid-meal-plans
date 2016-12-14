from __future__ import unicode_literals
from django.db import models
#from django.contrib.auth.models import User


# class PinUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     token = models.CharField(max_length=255)


class Pin(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    link = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    created_at = models.CharField(max_length=200)
    note = models.CharField(max_length=200)
    color = models.CharField(max_length=20)
    image = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    ''' other more complicated fields are shown in api docs '''

    def __str__(self):
        return self.url + " " + self.title


class MealDay(models.Model):
    date = models.CharField(max_length=20)

    def __str__(self):
        return self.date


class Meal(models.Model):
    url = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    meal_day = models.ForeignKey(MealDay, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " " + self.meal_day.date
