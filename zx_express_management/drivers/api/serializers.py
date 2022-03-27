from rest_framework import serializers
from zx_express_management.drivers.models import Drivers, TruckInfo, TruckType
from rest_framework.response import Response
from rest_framework import generics, status


class TruckInfoSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = TruckInfo
        fields = (
            "truck_number",
            "trailer_number",
            "refeer",
            "user",
        )


class TruckTypeSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = TruckType
        fields = (
            "truck_type_name",
            "user",
        )


class DriversService(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)
    truck_type = TruckTypeSerializer(read_only=True)
    truck_info = TruckInfoSerializer(read_only=True)

    class Meta:
        model = Drivers
        fields = (
            "user",
            "truck_type",
            "truck_info",
            "full_name",
            "phone_number",
        )
