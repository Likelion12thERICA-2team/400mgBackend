from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser) :
    """ 
    AbstractUser의 기본 제공 필드
    id, username, password, email, first_name, last_name
    """
    joinedDate = models.DateTimeField(auto_now_add=True)