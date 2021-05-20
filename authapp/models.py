from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='???????')
