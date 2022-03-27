from django.contrib import admin
from .models import TruckType, TruckInfo, Drivers, DriverNotes, TrailersToGo


class TruckTypeAdmin(admin.ModelAdmin):
    list_display = [
        "truck_type_name",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "truck_type_name",
        "created_at",
    ]
    filter_fields = [
        "truck_type_name",
        "created_at",
    ]


admin.site.register(TruckType, TruckTypeAdmin)


class TruckInfoAdmin(admin.ModelAdmin):
    list_display = [
        "truck_number",
        "trailer_number",
        "refeer",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "truck_number",
        "trailer_number",
        "refeer",
        "created_at",
    ]
    filter_fields = [
        "truck_number",
        "trailer_number",
        "refeer",
        "created_at",
    ]


admin.site.register(TruckInfo, TruckInfoAdmin)


class DriversAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "truck_type",
        "truck_info",
        "full_name",
        "phone_number",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "full_name",
        "phone_number",
    ]
    filter_fields = [
        "full_name",
        "phone_number",
        "created_at",
        "updated_at",
    ]


admin.site.register(Drivers, DriversAdmin)


class DriverNotesAdmin(admin.ModelAdmin):
    list_display = [
        "driver",
        "noted_by",
        "title",
        "note_content",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "title",
        "note_content",
    ]
    filter_fields = [
        "title",
        "note_content",
        "created_at",
        "updated_at",
    ]


admin.site.register(DriverNotes, DriverNotesAdmin)


class TrailersToGoAdmin(admin.ModelAdmin):
    list_display = [
        "driver",
        "asked",
        "place",
        "prefered_destination",
        "from_date",
        "to_date",
        "ready",
        "note",
        "active",
        "rejected",
        "created_at",
    ]
    search_fields = [
        "asked",
        "place",
        "prefered_destination",
        "from_date",
        "to_date",
        "ready",
        "note",
        "active",
        "rejected",
        "created_at",
    ]
    filter_fields = [
        "asked",
        "place",
        "prefered_destination",
        "from_date",
        "to_date",
        "ready",
        "note",
        "active",
        "rejected",
        "created_at",
    ]


admin.site.register(TrailersToGo, TrailersToGoAdmin)
