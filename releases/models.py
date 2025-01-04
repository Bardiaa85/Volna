from django.db import models
from artists.models import Artist
from django.core.validators import FileExtensionValidator
from mutagen import File
class Release(models.Model):
    title = models.CharField(max_length = 255 , verbose_name = "عنوان")
    cover_art = models.ImageField(upload_to = "releases/covers" , verbose_name = "کاور")
    audio_file = models.FileField(upload_to = "releases/audios" , validators = [FileExtensionValidator(allowed_extensions = ['mp3' , 'wav' , 'ogg'])] , verbose_name = "فایل صوتی")
    slug = models.SlugField(verbose_name = "پیوندک")
    artist = models.ForeignKey(Artist , on_delete = models.CASCADE , null = True , blank = True , verbose_name = "هنرمند" , related_name = "main_artist")
    release_date = models.DateTimeField(auto_now_add = True)
    views = models.PositiveIntegerField(default = 0 , verbose_name = "بازدید")
    features = models.ManyToManyField(Artist , blank = True , related_name = "features" , verbose_name = "همکاری ها")
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
    def full_artists_name(self):
        full_artists_name = str(self.artist)
        if self.features.count() != 0 :
            full_artists_name += " و "
            more_than_one_feature = False
            for artist in list(self.features.all()):
                if more_than_one_feature : 
                    full_artists_name += " و "
                full_artists_name += f"{artist.nickname}"
                more_than_one_feature = True
        return full_artists_name
    class Meta() :
        verbose_name = "منتشر شده"
        verbose_name_plural = "منتشر شده ها"