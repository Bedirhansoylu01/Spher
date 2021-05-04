from rest_framework import serializers
from django.conf import settings
from .models import Share

SHARE_ACTIONS = settings.SHARE_ACTIONS


class ShareActionSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    action = serializers.CharField()

    def validate_action(self, value):
        value = value.lower().strip()  # 'LIKE' -> 'like'
        if not value in SHARE_ACTIONS:
            raise serializers.ValidationError(
                "This is not a valid action for commits")
        return value


class ShareSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Share
        fields = ["id", "content", "likes", "user","parent"]

    def get_user(self, obj):
        return obj.user.username

    def get_likes(self, obj):
        return obj.likes.count()
   
    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > 250:
            raise serializers.ValidationError("This commit is too big")
        return content

class ShareSerializer_GET(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)
    parent=ShareSerializer(read_only=True)

    class Meta:
        model = Share
        fields = ["id", "content", "likes", "user","parent"]

    def get_user(self, obj):
        return obj.user.username

    def get_likes(self, obj):
        return obj.likes.count()
    