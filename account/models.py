from django.db import models
from django.contrib.auth.forms import User
from releases.models import Release
class Profile(models.Model):
    username = models.CharField(max_length = 255 , verbose_name = "نام کاربری") 
    full_name = models.CharField(max_length = 255 , verbose_name = "نام کامل")
    email_activation_code = models.CharField(max_length = 255 , verbose_name = "کد فعالسازی ایمیل")
    related_user = models.OneToOneField(User , on_delete = models.CASCADE , verbose_name = "کاربر مرتبط")
    favorites_list = models.ManyToManyField(Release , blank = True , related_name = "favorites_list" , verbose_name = "لیست علاقه‌مندی ها")
    def __str__(self):
        return self.username
    class Meta():
        verbose_name_plural = "پروفایل ها"
        verbose_name = "پروفایل"