from django.db import IntegrityError
from .serializers import (
    CompanyDriversSerializer,
    TruckInfoSerializer,
    TrailersToGoSerializer,
)
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from zx_express_management.users.api.serializers import UserSerializer
from django.db.models import Q
from zx_express_management.drivers.models import (
    Drivers,
    DriverTrucks,
    DriverNotes,
    TrailersToGo,
)
from .pagination import AnnouncementPagination


User = get_user_model()


class TruckAndDriverInfo(viewsets.ModelViewSet):
    pagination_class = AnnouncementPagination
    serializer_class = CompanyDriversSerializer
    queryset = Drivers.objects.all().order_by("-created_at")


class TrailersToGoClass(viewsets.ModelViewSet):
    pagination_class = AnnouncementPagination
    serializer_class = TrailersToGoSerializer
    queryset = TrailersToGo.objects.all().order_by("-created_at")

    def list(self, request):
        driver = Drivers.objects.get(user=request.user)
        queryset = TrailersToGo.objects.filter(driver=driver).order_by("-created_at")

        serializer = TrailersToGoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = TrailersToGoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateDriver(viewsets.ModelViewSet):
    pagination_class = AnnouncementPagination
    drivers = Drivers.objects.all().values_list("user", flat=True)
    queryset = (
        User.objects.filter(groups__name="driver")
        .exclude(Q(id__in=drivers))
        .order_by("-id")
    )
    serializer_class = UserSerializer

    def create(self, request):
        serializer = CompanyDriversSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
