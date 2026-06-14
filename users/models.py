from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    age = models.IntegerField()
    gender = models.CharField(max_length=20)

    height = models.FloatField()
    weight = models.FloatField()

    activity = models.CharField(max_length=50)

    hydration = models.BooleanField(default=False)
    sleep = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    habits = models.BooleanField(default=False)

    def __str__(self):
        return self.username
