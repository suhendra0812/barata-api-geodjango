from rest_framework.routers import DefaultRouter

from .views import WPPViewSet

router = DefaultRouter()

router.register(prefix="api/v1/wpp", viewset=WPPViewSet, basename="wpp")

urlpatterns = router.urls