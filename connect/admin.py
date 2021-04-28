from django.contrib import admin
from .models import share,Commit_Like
# Register your models here.

class Commit_LikeAdmin(admin.TabularInline):
    model=Commit_Like




class ShareAdmin(admin.ModelAdmin):
    inlines=[Commit_LikeAdmin]
    list_display=["__str__","user"]
    search_fields=["user__username","content"]

    class Meta:
        model=share

admin.site.register(share,ShareAdmin)