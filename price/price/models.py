from django.db import models
from django.core.validators import FileExtensionValidator


class Story(models.Model):
    image = models.ImageField(upload_to='price/')
    name = models.TextField(blank=True, null=True)
    symbol = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
