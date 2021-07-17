from django.db import models
from django.db.models import Q
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Commit_Like(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commit = models.ForeignKey('Share', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class ShareQuerySet(models.QuerySet):

    def by_username(self, username):
        return self.filter(user__username__iexact=username)


    def feed(self, user):
        profiles_exist = user.following.exists()
        followed_users_id = []
        if profiles_exist:
            followed_users_id = user.following.values_list("user__id", flat=True) # [x.user.id for x in profiles]
        return self.filter(
            Q(user__id__in=followed_users_id) |
            Q(user=user)
        ).distinct().order_by("-timestamp")                                                               #    def feed(self, user):


class ShareManager(models.Manager):
    
    def get_queryset(self, *args, **kwargs):
        return ShareQuerySet(self.model, using=self._db)

    def feed(self, user):
        return self.get_queryset().feed(user)

class Share(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="shares")
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    media_image = models.FileField(upload_to='media/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='commit_user', blank=True, through=Commit_Like)  # trough only for timestap

    objects = ShareManager()

    class Meta:
        ordering = ['-id']

    @property
    def is_recommit(self):
        return self.parent != None
