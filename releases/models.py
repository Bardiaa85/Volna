from django.db import models
from artists.models import Artist
from django.core.validators import FileExtensionValidator
from mutagen import File
class Release(models.Model):
    title = models.CharField(max_length = 255)
    cover_art = models.ImageField(upload_to = "releases/covers")
    audio_file = models.FileField(upload_to = "releases/audios" , validators = [FileExtensionValidator(allowed_extensions = ['mp3' , 'wav' , 'ogg'])])
    slug = models.SlugField()
    artist = models.ForeignKey(Artist , on_delete = models.CASCADE , null = True , blank = True)
    release_date = models.DateTimeField(auto_now_add = True)
    views = models.PositiveIntegerField(default = 0)
    def __str__(self):
        return self.title
    def get_audio_duration(self):
        audio = File(self.audio_file.path)
        if audio is not None and audio.info is not None:
            duration = int(audio.info.length)
            minutes, seconds = divmod(duration, 60)
            return f"{minutes}:{seconds:02d}"
        return "Unknown duration"
    def len_comments(self):
        return len(self.comment_set.all())
