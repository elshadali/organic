from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Account(AbstractUser):
    username = models.CharField(_('username'), max_length=255, blank=True, null=True)
    email = models.EmailField(_("email address"), unique=True, null=True)
    image = models.ImageField(upload_to='accounts', null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    

    class Meta:
        verbose_name = _("hesab")
        verbose_name_plural = _("hesablar")

    def __str__(self):
        return f"Account: {self.email}"