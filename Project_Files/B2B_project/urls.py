from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main_app.urls")),
    path("auth/", include("django.contrib.auth.urls")),
<<<<<<< HEAD
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 0d27bf3e06325fba4cd937e1cf224a743940528c
