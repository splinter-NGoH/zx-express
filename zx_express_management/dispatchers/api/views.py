from .serializers import DispatcherAnnouncementSerializer, DispatherProfileSerializer
from zx_express_management.dispatchers.models import DispatchersAnnouncement
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .pagination import AnnouncementPagination


class DispatcherAnnouncementClass(viewsets.ModelViewSet):
    pagination_class = AnnouncementPagination
    serializer_class = DispatcherAnnouncementSerializer
    queryset = DispatchersAnnouncement.objects.all().order_by("-created_at")
