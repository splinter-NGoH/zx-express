from rest_framework import serializers
from zx_express_management.drivers.models import (
    Drivers,
    TrailersToGo,
    DriverNotes,
    DriverTrucks,
)
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


# class TruckTypeSerializer(serializers.ModelSerializer):
#     user = serializers.CharField(source="user.username", read_only=True)

#     class Meta:
#         model = TruckType
#         fields = (
#             "truck_type_name",
#             "user",
#         )


class TruckInfoSerializer(serializers.ModelSerializer):
    drivername = serializers.CharField(source="driver.full_name", read_only=True)
    driveusername = serializers.CharField(source="driver.user.username", read_only=True)
    driver = serializers.CharField(source="driver.id", required=False)

    class Meta:
        model = DriverTrucks
        fields = (
            "id",
            "driver",
            "drivername",
            "driveusername",
            "truck_type_name",
            "truck_number",
            "trailer_number",
            "refeer",
            "active",
            "created_at",
            "updated_at",
        )


class CompanyDriversSerializer(serializers.ModelSerializer):
    truckinfo = TruckInfoSerializer(many=True)
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Drivers
        fields = (
            "id",
            "user",
            "username",
            "full_name",
            "phone_number",
            "birthdate",
            "created_at",
            "updated_at",
            "truckinfo",
        )

    def validate_user(self, user):
        if not user.groups.filter(name="driver"):
            raise serializers.ValidationError({"error": "user must be a driver"})
        return user

    def create(self, validated_data):
        truckinfos = validated_data.pop("truckinfo")
        driver = Drivers.objects.create(**validated_data)
        for truckinfo in truckinfos:
            DriverTrucks.objects.create(
                **truckinfo,
                driver=driver,
            )
        return driver


class TrailersToGoSerializer(serializers.ModelSerializer):
    driver_name = serializers.CharField(source="driver.full_name", read_only=True)

    class Meta:
        model = TrailersToGo
        fields = (
            "id",
            "driver_name",
            "driver",
            "asked",
            "emptyplace",
            "prefered_destination",
            "from_date",
            "to_date",
            "ready",
            "note",
            "active",
            "rejected",
            "created_at",
        )
        read_only_fields = ("created_at",)
