from rest_framework import serializers
from .models import Post, Reply, Scrap


class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    reply_count = serializers.SerializerMethodField()
    scrap_count = serializers.SerializerMethodField()
    is_scraped = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'username', 'subject', 'content', 'post_date',
                  'image', 'reply_count', 'scrap_count', 'is_scraped')
        read_only_fields = ('id', 'post_date', 'username',
                            'reply_count', 'scrap_count', 'is_scraped')

    def get_reply_count(self, obj):
        return Reply.objects.filter(post=obj).count()

    def get_scrap_count(self, obj):
        return Scrap.objects.filter(post=obj).count()

    def get_is_scraped(self, obj):
        request = self.context.get('request')
        if request.user.is_authenticated:
            return Scrap.objects.filter(user=request.user, post=obj).exists()
        return False


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
