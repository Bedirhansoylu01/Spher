from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Commit_Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commit = models.ForeignKey('share', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    media_image = models.FileField(upload_to='media/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='commit_user', blank=True, through=Commit_Like)  # trough only for timestap

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.content
