from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.

class CustomUser(User):
    nickname = models.CharField(max_length=100, null=True, blank=True)
    statement = models.TextField()
    # Use UserManager to get the create_user method, etc.
    objects = UserManager()