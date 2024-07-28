from .models import CaffeinIntake
from rest_framework.views import APIView
from .serializers import CaffeinIntakeSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT

# Create your views here.
class CaffeinIntakes(APIView):
    def get_objects(self, user_id) :
        try :
            caffeinIntake = CaffeinIntake.objects.filter(user_id=user_id)
        except :
            raise NotFound
        return caffeinIntake

    def get(self, request, user_id):
        caffeinIntake = self.get_objects(user_id) 
        serializer = CaffeinIntakeSerializer(caffeinIntake, many=True) 
        return Response(serializer.data)
    
    def post(self, request, user_id): 
        caffeinIntake = self.get_objects(user_id)
        serializer = CaffeinIntakeSerializer(caffeinIntake, data=request.data, partial=True, many=True) 
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)