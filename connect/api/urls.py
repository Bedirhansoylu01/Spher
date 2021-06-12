from django.urls import path
from .views import (shareView, commit_list, shareactionview,
                    commit_detail, commit_delete)
urlpatterns = [

    path("share", shareView),
    path("share_ls", commit_list),
    path("share/action", shareactionview),
    path("share/<int:share_id>", commit_detail),
    path("share/<int:pk>/delete", commit_delete),
]
