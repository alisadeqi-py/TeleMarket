from django.db import models
from django.core.validators import FileExtensionValidator


class Story(models.Model):
    MARKET_CHOICES = [
        ('Forex', 'Forex'),
        ('Crypto', 'Crypto'),
        ('TSE', 'Tehran Stock Exchange'),
        ('GOLDEN', 'GOLDEN'),
    ]
    
    image = models.ImageField(upload_to='stories/')
    caption = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  # For expiring after 24 hours
    market = models.CharField(max_length=20, choices=MARKET_CHOICES)



class ExplorePost(models.Model):
    file = models.FileField(
        upload_to='posts/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'mp4', 'mov', 'avi'])],
        help_text="Upload an image (jpg, jpeg, png) or video (mp4, mov, avi)."
    )
    caption = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_pinned = models.BooleanField(default=False)

    def total_likes(self):
        return self.likes.count()

    def is_image(self):
        """Check if the file is an image based on its extension."""
        return self.file.name.split('.')[-1].lower() in ['jpg', 'jpeg', 'png']

    def is_video(self):
        """Check if the file is a video based on its extension."""
        return self.file.name.split('.')[-1].lower() in ['mp4', 'mov', 'avi']
