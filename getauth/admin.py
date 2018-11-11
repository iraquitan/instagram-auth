from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import InstagramUser


# Register your models here.
@admin.register(InstagramUser)
class InstagramUserAdmin(admin.ModelAdmin):
    verbose_name = _("instagram user")
    verbose_name_plural = _("instagram users")
