from rest_framework.routers import DefaultRouter

from .views import ShipViewSet

router = DefaultRouter()

router.register(prefix="api/v1/ship", viewset=ShipViewSet, basename="ship")

urlpatterns = router.urls