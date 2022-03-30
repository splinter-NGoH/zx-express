from django.contrib import admin
from .models import DispatcherProfile, DispatchersAnnouncement


class DispatcherProfileAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "full_name",
        "phone_number",
        "start_shift",
        "end_shift",
        "notes",
        "created_at",
    ]
    search_fields = [
        "full_name",
        "phone_number",
        "start_shift",
        "end_shift",
        "notes",
        "created_at",
    ]
    filter_fields = [
        "full_name",
        "phone_number",
        "start_shift",
        "end_shift",
        "notes",
        "created_at",
    ]

    ordering = ("-created_at",)


admin.site.register(DispatcherProfile, DispatcherProfileAdmin)


class DispatchersAnnouncementAdmin(admin.ModelAdmin):
    list_display = [
        "dispatcher",
        "title",
        "content",
        "created_at",
    ]
    search_fields = [
        "title",
        "content",
        "created_at",
    ]
    filter_fields = [
        "title",
        "content",
        "created_at",
    ]

    ordering = ("-created_at",)


admin.site.register(DispatchersAnnouncement, DispatchersAnnouncementAdmin)
