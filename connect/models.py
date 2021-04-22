from django.db import models
from django.conf import settings


class share(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    media_image = models.FileField(upload_to='media/', blank=True, null=True)
    
    class Meta:
        ordering=["-id"]
    
    def __str__(self):
        return self.content
    