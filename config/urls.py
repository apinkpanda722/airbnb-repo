from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import path
>>>>>>> cc2656b759cba23d39d51007debe9d5b6390a042
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
<<<<<<< HEAD
    path("api/v1/rooms/", include("rooms.urls")),
    path("api/v1/users/", include("users.urls")),
=======
>>>>>>> cc2656b759cba23d39d51007debe9d5b6390a042
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
