from django.urls import path
from .views import home,commit_list,commit_detail,shareView,commit_delete,shareactionview

urlpatterns = [
    path("", home),
    path("share",shareView),
    path("share_ls",commit_list),
    path("api/share/action",shareactionview),
    path("api/share/<int:share_id>",commit_detail),
    path("api/share/<int:pk>/delete",commit_delete),    
    ]
