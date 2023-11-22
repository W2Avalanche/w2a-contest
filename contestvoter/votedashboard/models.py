from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class VideoElement(models.Model):
    title = models.CharField(max_length=100)
    youtube_url = models.URLField()
    text = models.TextField()
    total_votes = models.IntegerField()

class Votes(models.Model):
    voted_for = models.ForeignKey(VideoElement, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)