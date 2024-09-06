from django.db import models
class Artist(models.Model) :
    nickname = models.CharField(max_length = 255 , verbose_name = "نام مستعار")
    image = models.ImageField(upload_to = "artists" , verbose_name = "تصویر")
    slug = models.SlugField(verbose_name = "پیوندک")
    description = models.TextField(verbose_name = "توضیحات")
    def __str__(self):
        return self.nickname
    class Meta():
        verbose_name_plural = "هنرمندان"
        verbose_name = "هنرمند"