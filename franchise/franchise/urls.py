from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from core import views as core_views

router = routers.DefaultRouter()
router.register(r'collectable', core_views.CollectableViewSet)
router.register(r'collectable-franchise', core_views.CollectableFranchiseViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
