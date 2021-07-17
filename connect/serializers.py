from rest_framework import serializers
from django.conf import settings
from .models import Share
from profiles.serializers import PublicProfileSerializer


SHARE_ACTIONS = settings.SHARE_ACTIONS


class ShareActionSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    action = serializers.CharField()

    def validate_action(self, value):
        
        if not value in SHARE_ACTIONS:
            raise serializers.ValidationError(
                "This is not a valid action for commits")
        return value



class ShareSerializer_POST(serializers.ModelSerializer):
    user = PublicProfileSerializer(source='user.profile',read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Share
        fields = ["user","id", "content",
        "likes","timestamp"]


    def get_likes(self, obj):
        return obj.likes.count()
    
    def validate_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > 250:
            raise serializers.ValidationError("This commit is too big")
        return content



class ShareSerializer(serializers.ModelSerializer):
    user = PublicProfileSerializer(source='user.profile',read_only=True)#serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    parent = ShareSerializer_POST(read_only=True)


    class Meta:
        model = Share
        fields = ["user","id", "content",
        "likes","is_recommit","parent","timestamp"]

    def get_likes(self, obj):
        return obj.likes.count()


