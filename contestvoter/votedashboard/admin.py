from django.contrib import admin

# Register your models here.
from .models import VideoElement, Votes
class VideoElementAdmin(admin.ModelAdmin):
    list_display = ('title', 'youtube_url', 'text')
    search_fields = ('title', 'text')
class VoteElementAdmin(admin.ModelAdmin):
    list_display = ('voted_by', 'voted_for')
admin.site.register(VideoElement, VideoElementAdmin)
admin.site.register(Votes, VoteElementAdmin)