from zx_express_management.dispatchers.models import (
    DispatcherProfile,
    DispatchersAnnouncement,
)
from rest_framework import serializers


class DispatcherAnnouncementSerializer(serializers.ModelSerializer):
    dispatcher_id = serializers.CharField(source="dispatcher.id", read_only=True)
    dispatcher = serializers.CharField(source="dispatcher.full_name", read_only=True)

    class Meta:
        model = DispatchersAnnouncement
        fields = (
            "id",
            "dispatcher_id",
            "dispatcher",
            "title",
            "content",
            "created_at",
        )


class DispatherProfileSerializer(serializers.ModelSerializer):
    dispatchers_announcements = DispatcherAnnouncementSerializer(many=True)

    class Meta:
        model = DispatcherProfile
        fields = (
            "id",
            "user",
            "full_name",
            "notes",
            "phone_number",
            "start_shift",
            "end_shift",
            "created_at",
        )
