from django.contrib import admin
from .models import share
# Register your models here.
class ShareAdmin(admin.ModelAdmin):
    list_display=["__str__","user"]
    search_fields=["user__username","content"]
    class Meta:
        model=share

admin.site.register(share,ShareAdmin)