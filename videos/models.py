from django.db import models
from django.utils import timezone

from accounts.models import User


class Video(models.Model):
    file = models.FileField(default='', upload_to='')
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(default='No description yet ...')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    banned = models.BooleanField(default=False)  # To see if the video is banned or not

    def __str__(self):
        return self.title

    def ban(self):
        self.banned = True
        self.save()


class Comment(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)


class Tag(models.Model):
    videos = models.ManyToManyField(Video)


class Ticket(models.Model):
    TICKET_STATUS = (
        ("n", "new"),
        ("w", "waiting"),
        ("s", "solved"),
        ("c", "closed")
    )
    title = models.CharField(max_length=30)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=TICKET_STATUS, default="n")
