from .models import CaffeinIntake
from rest_framework.views import APIView
from .serializers import CaffeinIntakeSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated
from .utils import process_caffeine_intake
from datetime import datetime, timedelta

# Create your views here.


class CaffeinIntakes(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response(status=HTTP_401_UNAUTHORIZED)

        day_ago = datetime.now() - timedelta(hours=24)
        # 현재 시간 기준으로 이전 24시간동안의 카페인 섭취량 가져옴
        caffeinIntake = CaffeinIntake.objects.filter(
            user=user, time__gte=day_ago)
        serializer = CaffeinIntakeSerializer(caffeinIntake, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response(status=HTTP_401_UNAUTHORIZED)

        # 요청 데이터 예시:
        # {
        #   "time": "2024-07-18T14:30:00Z",
        #   "amount": 95,
        #   "caffeinType": "커피"
        # }

        # TODO: 요청 데이터 검증 필요

        data = request.data

        data['user'] = user.id

        # TODO: 현재는 단일 데이터만 처리하도록 구현되어 있음
        # 다수의 데이터를 처리할 수 있도록 수정 필요
        serializer = CaffeinIntakeSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class CaffeinePredictionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if not user.is_authenticated:
            return Response(status=HTTP_401_UNAUTHORIZED)
        # 현재 시간 기준으로 이전 12시간동안의 카페인 섭취량 가져옴
        twelve_hours_ago = datetime.now() - timedelta(hours=12)

        caffeinIntake = CaffeinIntake.objects.filter(
            user=user, time__gte=twelve_hours_ago).order_by('time')

        intake_list = [(int((intake.time.timestamp() - twelve_hours_ago.timestamp()) / 60), intake.amount)
                       for intake in caffeinIntake]
        total_time = 12 * 60  # 12시간
        caffeine_levels = process_caffeine_intake(intake_list, total_time)
        return Response(caffeine_levels)


# 월별로 카페인 섭취량을 가져오는 API
# 하루의 총 카페인 섭취량 계산
class MonthlyCaffeineIntakeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, year, month):
        user = request.user

        if not user.is_authenticated:
            return Response(status=HTTP_401_UNAUTHORIZED)

        # 해당 월의 첫날과 마지막날을 구함
        first_day = datetime(year, month, 1)
        if month == 12:
            last_day = datetime(year + 1, 1, 1)
        else:
            last_day = datetime(year, month + 1, 1)

        # 해당 월의 카페인 섭취량을 가져옴
        caffeinIntake = CaffeinIntake.objects.filter(
            user=user, time__gte=first_day, time__lt=last_day).order_by('time')

        daily_intake = {}
        for intake in caffeinIntake:
            day = intake.time.day
            if day in daily_intake:
                daily_intake[day] += intake.amount
            else:
                daily_intake[day] = intake.amount

        # 일별 카페인 섭취량을 정렬하여 반환
        sorted_intake = sorted(daily_intake.items())
        return Response(dict(sorted_intake))
