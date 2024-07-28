from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin) :
    list_display = ("id", "password", "username", "email", "first_name", "last_name", "joinedDate")