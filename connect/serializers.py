from rest_framework import serializers
from .models import share

class ShareSerializer_POST(serializers.ModelSerializer):
    class Meta:
        model=share
        fields=["content"]
        
        def clean_content(self):
            content=self.cleaned_data.get("content")
            if len(content)>250:
                raise serializers.ValidationError("This commit is too big")
            return content    


class ShareSerializer_GET(serializers.ModelSerializer):
    class Meta:
        model=share
        fields=["id","user","content"]
        