from django.db import IntegrityError
from .serializers import DriversService, TruckInfoSerializer, TruckTypeSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from zx_express_management.drivers.models import Drivers, TruckInfo, TruckType

User = get_user_model()


class Truck_type_name(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        drivers = TruckType.objects.all()
        serializer = TruckTypeSerializer(
            drivers,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = TruckTypeSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except IntegrityError:
            return Response(
                {"IntegrityError": "cant add more than 1 value for each user"},
            )


class TruckInfo_name(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        drivers = TruckInfo.objects.all()
        serializer = TruckInfoSerializer(
            drivers,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = TruckInfoSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response(
                {"IntegrityError": "cant add more than 1 value for each user"},
            )


class Add_driver_to_user(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        drivers = Drivers.objects.all()
        serializer = DriversService(
            drivers,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        truck_type = TruckType.objects.get(user=request.user)
        truck_info = TruckInfo.objects.get(user=request.user)
        serializer = DriversService(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save(
                    user=request.user, truck_type=truck_type, truck_info=truck_info
                )
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response(
                {"IntegrityError": "cant add more than 1 value for each user"},
            )
