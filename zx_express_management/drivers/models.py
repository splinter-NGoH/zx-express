from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class TruckType(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    truck_type_name = models.CharField(max_length=254, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Truck type")
        verbose_name_plural = _("Truck types")

    def __str__(self):
        return self.truck_type_name


class TruckInfo(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    truck_number = models.BigIntegerField(unique=True)
    trailer_number = models.BigIntegerField(unique=True)
    refeer = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Truck Info")
        verbose_name_plural = _("Trucks Info")

    def __str__(self):
        return str(self.truck_number)


class Drivers(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    truck_type = models.ForeignKey(
        TruckType,
        on_delete=models.CASCADE,
    )
    truck_info = models.OneToOneField(TruckInfo, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=254)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True
    )  # Validators should be a list
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Driver")
        verbose_name_plural = _("Drivers")

    def __str__(self):
        return self.full_name


class DriverNotes(models.Model):
    driver = models.ForeignKey(Drivers, on_delete=models.CASCADE)
    noted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
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
        Drivers,
        on_delete=models.CASCADE,
    )
    asked = models.BooleanField(default=False)
    place = models.CharField(max_length=254)
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
