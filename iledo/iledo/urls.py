from django.contrib import admin
from django.urls import path
from main.views import mainpage
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers
from main.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainpage),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
