from django.db import models
from users.models import CustomUser as User

# Create your models here.


class CaffeinIntake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user 엔티티에서 userId를 외래키로 가져옴
    # intakeId = models.CharField(max_length=255, primary_key=True)
    intake_id = models.AutoField(primary_key=True)
    time = models.DateTimeField()
    amount = models.FloatField()
    caffeinType = models.CharField(max_length=50)
