from rest_framework import serializers
from .models import Post, Reply, Scrap


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'subject', 'content', 'post_date')
        read_only_fields = ('id', 'post_date', 'user')


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('id', 'post', 'user', 'content', 'reply_date')
        read_only_fields = ('id', 'reply_date', 'user', 'post')


class ScrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scrap
        fields = ('id', 'user', 'post', 'created_at')
        read_only_fields = ('id', 'created_at', 'user', 'post')
