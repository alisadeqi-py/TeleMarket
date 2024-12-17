from django.db import models
from account.models import CustomUser
from django.conf import settings
import uuid
# Create your models here.


from django.db import models
from django.conf import settings
import uuid

class Channel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_channels"
    )
    is_free = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Optional price
    image = models.ImageField(upload_to='channel_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    new_message_timestamp = models.DateTimeField(auto_now=True)

    # New field to link subscribed students to channels
    subscribers = models.ManyToManyField(
        'account.StudentProfile',  # Assuming there's a `StudentProfile` model
        related_name="subscribed_channels",
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class Post(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    media_file = models.URLField(null=True, blank=True)  # AWS S3 file URL
    scheduled_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="posts")
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return f"Post in {self.channel.name} by {self.created_by.username}"



