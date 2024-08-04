from rest_framework import serializers
from .models import Follow
import datetime


class FollowSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    last_caffeine_intake = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Follow
        fields = ('user', 'username', 'follower',
                  'last_caffeine_intake', 'status')
        read_only_fields = ('user', 'username', 'follower',
                            'last_caffeine_intake', 'status')

    def get_username(self, obj):
        return obj.user.username

    def get_last_caffeine_intake(self, obj):
        last_intake = obj.user.caffeinintake_set.order_by('-time').first()
        if last_intake:
            return last_intake.time
        return None

    def get_status(self, obj):
        # TODO: 현재는 총 섭취량을 기준으로 상태를 판단하도록 구현되어 있음
        # 예측된 카페인 섭취량을 기준으로 상태를 판단하도록 수정 필요
        caffine_intakes = obj.user.caffeinintake_set.filter(
            time__gte=datetime.datetime.now() - datetime.timedelta(hours=24)).order_by('-time')
        total_caffeine = sum([intake.amount for intake in caffine_intakes])


# 0~50mg 보통
# 50mg~150mg 집중
# 150~250mg 각성
# 250~400mg 과잉
# 400mg~600mg 한계

        if total_caffeine < 50:
            return "보통"
        elif total_caffeine < 150:
            return "집중"
        elif total_caffeine < 250:
            return "각성"
        elif total_caffeine < 400:
            return "과잉"
        else:
            return "한계"
