from django.db import models

# Create your models here.
class Video(models.Model):
    video_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title