from django.db import models

# Create your models here.


#importes 
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=150, unique=True)
    
    
    USERNAME_FIELD = 'email'  # new
    
    REQUIRED_FIELDS = ['username', 'password']  # new