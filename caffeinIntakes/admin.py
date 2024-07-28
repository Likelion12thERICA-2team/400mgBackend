from django.contrib import admin
from .models import CaffeinIntake

# Register your models here.
@admin.register(CaffeinIntake)
class CaffeinIntakeAdmin(admin.ModelAdmin) :
    list_display = ("user", "intakeId", "time", "amount", "caffeinType")