from gettext import NullTranslations
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from zx_express_management.dispatchers.models import DispatcherProfile


User = get_user_model()


# class TruckInfo(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#     )
#     truck_number = models.BigIntegerField(unique=True)
#     trailer_number = models.BigIntegerField(unique=True)
#     refeer = models.CharField(max_length=254)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name = _("Truck Info")
#         verbose_name_plural = _("Trucks Info")

#     def __str__(self):
#         return str(self.truck_number)


class Drivers(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    dispatchers = models.ForeignKey(
        DispatcherProfile,
        on_delete=models.SET_NULL,
        null=True,
        related_name="drivers_with_dispatcher",
    )

    full_name = models.CharField(max_length=254)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True
    )  # Validators should be a list
    birthdate = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Driver")
        verbose_name_plural = _("Drivers")

    def __str__(self):
        return self.full_name


class DriverTrucks(models.Model):
    driver = models.ForeignKey(
        Drivers, on_delete=models.CASCADE, related_name="truckinfo"
    )
    truck_type_name = models.CharField(max_length=254, blank=True)
    truck_number = models.BigIntegerField(blank=True)
    trailer_number = models.BigIntegerField(blank=True)
    refeer = models.CharField(max_length=254, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Truck type")
        verbose_name_plural = _("Truck types")

    def __str__(self):
        return self.truck_type_name


class DriverNotes(models.Model):
    driver = models.ForeignKey(
        Drivers, on_delete=models.CASCADE, related_name="notes_on_driver"
    )
    title = models.CharField(max_length=245, blank=True)
    note_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Driver Note")
        verbose_name_plural = _("Driver Notes")

    def __str__(self):
        return self.title


# class Location(models.Model):
#     place = models.CharField(max_length=254)
#     status = models.CharField(max_length=254)
#     note = models.TextField(blank=True)

#     class Meta:
#         verbose_name = _("Location")
#         verbose_name_plural = _("Locations")

#     def __str__(self):
#         return self.place


class TrailersToGo(models.Model):
    driver = models.ForeignKey(
        Drivers, on_delete=models.CASCADE, related_name="trailers_to_go"
    )
    asked = models.BooleanField(default=False)
    emptyplace = models.CharField(max_length=254, blank=True)
    prefered_destination = models.CharField(max_length=254, blank=True)
    from_date = models.DateTimeField(blank=True)
    to_date = models.DateTimeField(blank=True)
    ready = models.BooleanField(default=False)
    note = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    rejected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Trailer To Go")
        verbose_name_plural = _("Trailers To Go")

    def __str__(self):
        return self.driver.full_name
