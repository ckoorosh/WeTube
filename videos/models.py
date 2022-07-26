from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.files.storage import default_storage

from accounts.models import User


class Video(models.Model):
    file = models.FileField(default='', upload_to='')
    title = models.CharField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(default='No description yet ...')
    views = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='likes')
    likes_count = models.IntegerField(default=0)
    dislikes = models.ManyToManyField(User, related_name='dislikes')
    dislikes_count = models.IntegerField(default=0)
    banned = models.BooleanField(default=False)  # To see if the video is banned or not

    def __str__(self):
        return self.title

    def ban(self):
        self.banned = True
        self.save()

    def get_url(self):
        return default_storage.exists(self.file.path)


class Comment(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)


class Tag(models.Model):
    videos = models.ManyToManyField(Video)


class TicketResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)


class Ticket(models.Model):
    TICKET_STATUS = (
        ("n", "new"),
        ("w", "waiting"),
        ("s", "solved"),
        ("c", "closed")
    )
    title = models.CharField(max_length=30)
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=TICKET_STATUS, default="n")
    response = models.ForeignKey(TicketResponse, on_delete=models.CASCADE, blank=True, null=True)
