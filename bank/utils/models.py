from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(_("date joined"), auto_now_add=True)
    update_at = models.DateTimeField(_("update date"), auto_now=True)

    class Meta:
        abstract = True
