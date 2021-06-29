from django.db import models
from django.core.validators import RegexValidator

# Create User model to store contacts
class Users(models.Model):
    email = models.EmailField(primary_key=True)
    name = models.TextField(default=None)
    phone_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')]) #10 digit number validation
    address = models.TextField()
