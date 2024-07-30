from django.db import models
class Artist(models.Model) :
    nickname = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = "artists")
    slug = models.SlugField()
    description = models.TextField()
    def __str__(self):
        return self.nickname
