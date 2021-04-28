from rest_framework import serializers
from django.conf import settings
from .models import share

SHARE_ACTIONS = settings.SHARE_ACTIONS


class ShareActionSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    action = serializers.CharField()

    def validate_action(self, value):
        action = value.lower().strip()  # 'LIKE' -> 'like'
        if not action in SHARE_ACTIONS:
            raise serializers.ValidationError(
                "This is not a valid action for commits")
        return action


class ShareSerializer(serializers.ModelSerializer):
    likes=serializers.SerializerMethodField(read_only=True)
    user=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = share
        fields = ["id","content","likes","user"]
    def get_user(self,obj):
        return obj.user.username 

    def get_likes(self,obj):
        return obj.likes.count()  
        
    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > 250:
            raise serializers.ValidationError("This commit is too big")
        return content
