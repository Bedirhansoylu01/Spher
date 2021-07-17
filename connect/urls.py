from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,re_path
from django.urls.conf import include
from .views import (home_view,spher_list_view,
                    spher_detail_view)
from accounts.views import (login_view,
                        register_view,
                        logout_view,)

urlpatterns = [
    path("",home_view),
    path("global/", spher_list_view),
    path("login/",login_view),
    path("logout/",logout_view),
    path("register/",register_view),
    path('<int:share_id>',spher_detail_view),
    re_path(r'profiles?/',include('profiles.urls')),
    path("list",spher_list_view),
    path('api/',include('connect.api.urls')),
    re_path(r'api/profiles?/',include('profiles.api.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
