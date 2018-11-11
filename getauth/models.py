import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class InstagramUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    access_token = models.CharField(_("access token"), max_length=255)
    social_id = models.CharField(_("social id"), max_length=255)
    username = models.CharField(_("username"), max_length=255)
    full_name = models.CharField(_("full name"), max_length=255)
    profile_picture = models.CharField(_("profile picture"), max_length=500)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
