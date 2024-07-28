from rest_framework.serializers import ModelSerializer
from .models import CaffeinIntake

class CaffeinIntakeSerializer(ModelSerializer) :
    class Meta :
        model = CaffeinIntake
        fields = "__all__"