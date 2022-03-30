from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from zx_express_management.users.api.views import UserViewSet
from zx_express_management.dispatchers.api.views import DispatcherAnnouncementClass
from zx_express_management.drivers.api.views import (
    TruckAndDriverInfo,
    CreateDriver,
    TrailersToGoClass,
)

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()
from rest_framework.routers import DefaultRouter

router.register("trailerstogo", TrailersToGoClass, basename="ready")
router.register("drivertrucksinfo", TruckAndDriverInfo, basename="truck")
router.register(
    "announcement", DispatcherAnnouncementClass, basename="announcementdispatcher"
)
router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls
