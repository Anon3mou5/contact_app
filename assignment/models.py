from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Users(models.Model):
    email = models.TextField(primary_key=True)
    name = models.TextField(default=None)
    phone_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    address = models.TextField()

    # def __init__(self, *initial_data, **kwargs):
    #     for dictionary in initial_data:
    #         for key in dictionary:
    #             setattr(self, key, dictionary[key])
    #     for key in kwargs:
    #         setattr(self, key, kwargs[key])
