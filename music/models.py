from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_premium = models.BooleanField(default=False)


class Song(models.Model):
    title = models.CharField(max_length=255)
    duration = models.FloatField()
    album = models.ForeignKey('Album', on_delete=models.CASCADE, related_name='songs')


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    songs = models.ManyToManyField(Song, related_name='playlists')


class Album(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='albums')


class Artist(models.Model):
    name = models.CharField(max_length=255)

