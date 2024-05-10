# users/models.py
from django.db import models

class User(models.Model):
    first_name = models.CharField("Name", max_length=50)
    last_name = models.CharField("Last_name", max_length=50)
    username = models.CharField("username", max_length=50, unique=True)
    password = models.CharField("password", max_length=100)
    phone_number = models.CharField("Phone_number", max_length=30, unique=True, null=True, blank=True)

    def __str__(self):
        return f'{self.username}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, upload_to="img/", blank=True)
    about = models.CharField(max_length=500)
   
    def __str__(self):
        return self.user


