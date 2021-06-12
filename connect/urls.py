from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls.conf import include
from django.views.generic import TemplateView
from .views import (home, spher_list_view,
                    spher_detail_view, spher_profile_view)


urlpatterns = [
    path("", spher_list_view),
    path("react/", TemplateView.as_view(template_name='react_via_dj.html')),
    path('<int:share_id>',spher_detail_view),
    path('profile/<str:username>',spher_profile_view),
    path("list",spher_list_view),
    path('api/',include('connect.api.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
