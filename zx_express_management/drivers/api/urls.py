from django.urls import path

from .views import Add_driver_to_user, Truck_type_name, TruckInfo_name

urlpatterns = [
    path(
        "drivers/truck_type_name/",
        Truck_type_name.as_view(),
        name="truck_type_name",
    ),
    path(
        "drivers/TruckInfo_name/",
        TruckInfo_name.as_view(),
        name="TruckInfo_name",
    ),
    path(
        "drivers/",
        Add_driver_to_user.as_view(),
        name="drivers",
    ),
]
