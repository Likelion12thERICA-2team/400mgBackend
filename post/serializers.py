from rest_framework import serializers
from .models import Post
from .models import Scrap

class ScrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrap
        fields = ['id', 'user', 'post', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
