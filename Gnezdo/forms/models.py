from django.db import models
from django.conf import settings
# Create your models here.

class BaseForm(models.Model):
    text = models.TextField(null=True, default='')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.text

class SeekerForm(BaseForm):
    aditionalText = models.TextField(null=True, default='')

class OwnerForm(BaseForm):
    aditionalText = models.TextField(null=True, default='')
