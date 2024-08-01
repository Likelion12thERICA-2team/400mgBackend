from rest_framework.serializers import ModelSerializer
from .models import CaffeinIntake


class CaffeinIntakeSerializer(ModelSerializer):
    class Meta:
        model = CaffeinIntake
        fields = ('time', 'amount', 'caffeinType', 'user')
