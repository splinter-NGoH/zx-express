from django.contrib import admin
from .models import Drivers, DriverNotes, TrailersToGo, DriverTrucks


class DriverTrucksAdmin(admin.ModelAdmin):
    list_display = [
        "driver",
        "truck_type_name",
        "truck_number",
        "trailer_number",
        "refeer",
        "active",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "truck_type_name",
        "truck_number",
        "trailer_number",
        "refeer",
        "active",
    ]
    filter_fields = [
        "truck_type_name",
        "truck_number",
        "trailer_number",
        "refeer",
        "active",
        "created_at",
    ]


admin.site.register(DriverTrucks, DriverTrucksAdmin)


class DriversAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "full_name",
        "phone_number",
        "birthdate",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "full_name",
        "phone_number",
        "birthdate",
    ]
    filter_fields = [
        "full_name",
        "phone_number",
        "birthdate",
        "created_at",
        "updated_at",
    ]


admin.site.register(Drivers, DriversAdmin)


class DriverNotesAdmin(admin.ModelAdmin):
    list_display = [
        "driver",
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
        "emptyplace",
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
        "emptyplace",
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
        "emptyplace",
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
