from django.contrib import admin
from . import models


class VideoPostAdmin(admin.ModelAdmin):
    search_fields = ('date',)


class PosterAdmin(admin.ModelAdmin):
    search_fields = ('last_name',)


admin.site.register(models.VideoPost, VideoPostAdmin)
admin.site.register(models.Poster, PosterAdmin)
