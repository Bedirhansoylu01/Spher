from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from .views import (home, spher_list_view,
                    spher_detail_view, spher_profile_view,
                    commit_list, commit_detail, shareView,
                    commit_delete, shareactionview)


urlpatterns = [
    path("", home),
    path("react/", TemplateView.as_view(template_name='react_via_dj.html')),
    path('<int:share_id>',spher_detail_view),
    path('profile/<str:username>',spher_profile_view),
    path("list",spher_list_view),
#___________________________________________________________________________________________________________
    path("api/share", shareView),
    path("api/share_ls", commit_list),
    path("api/share/action", shareactionview),
    path("api/share/<int:share_id>", commit_detail),
    path("api/share/<int:pk>/delete", commit_delete),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
