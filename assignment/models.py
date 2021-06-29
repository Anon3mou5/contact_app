from django.db import models

# Create your models here.

class User(models.Model):
    email = models.TextField(primary_key=True)
    name = models.TextField(default=None)
    phone_number = models.IntegerField(max_length=10)
    address = models.TextField()

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])
