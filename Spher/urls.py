from django.contrib import admin
from django.urls import path
from connect.views import home,commit_list,commit_detail,shareView,commit_delete

urlpatterns = [
    path("", home),
    path("share",shareView),
    path("data/",commit_list),
    path("data/<int:share_id>",commit_detail),
    path("data/<int:pk>/delete",commit_delete),    
    path('admin/', admin.site.urls) ]
