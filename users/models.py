from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100, blank=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

class Profile(models.Model):
    GENDER = (
        ('1','男性'),
        ('2','女性'),
    )
    username = models.CharField(max_length=20, unique=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    gender = models.CharField(blank=True, max_length=1, choices=GENDER)
    birth = models.DateField(blank=True)
    address = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=9, blank=True)
    image = models.ImageField(upload_to='image/user/', blank=True)

    def __str__(self):
        return self.username
