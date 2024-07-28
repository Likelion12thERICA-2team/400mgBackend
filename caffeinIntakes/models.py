from django.db import models

# Create your models here.
class CaffeinIntake(models.Model) :
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    # user 엔티티에서 userId를 외래키로 가져옴
    intakeId = models.CharField(max_length=255,primary_key=True)
    time = models.DateTimeField(auto_now=True)
    amount = models.FloatField()
    caffeinType = models.CharField(max_length=50)