from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class DispatcherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True
    )  # Validators should be a list
    birthdate = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=254)
    start_shift = models.CharField(max_length=254)
    end_shift = models.CharField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Dispatcher Profile")
        verbose_name_plural = _("Dispatchers Profile")

    def __str__(self):
        return self.full_name


class DispatchersAnnouncement(models.Model):
    dispatcher = models.ForeignKey(
        DispatcherProfile,
        on_delete=models.CASCADE,
        related_name="dispatchers_announcements",
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Dispatcher Announcement")
        verbose_name_plural = _("Dispatchers Announcement")

    def __str__(self):
        return self.title
