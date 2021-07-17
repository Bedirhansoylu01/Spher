from django.urls import path
from .views import (shareView, commit_list,commit_feed, shareactionview,
                    commit_detail, commit_delete)
urlpatterns = [

    path("share", shareView),
    path("feed",commit_feed),  
    path("share_ls", commit_list),
    path("share/action", shareactionview),
    path("share/<int:share_id>", commit_detail),
    path("share/<int:pk>/delete", commit_delete),
]
