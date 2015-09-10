from django.db import models
from embed_video.fields import EmbedVideoField


class VideoPost(models.Model):
    video = EmbedVideoField(null=False, blank=False)
    comment = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=False, blank=False)
 


class Poster(models.Model):
	first_name = models.CharField(max_length=50, null=False, blank=False)
	last_name = models.CharField(max_length=50, null=False, blank=False)
	email = models.EmailField(max_length=254, null=False, blank=False)
	posts = models.ManyToManyField('VideoPost', null=False, blank=False)
