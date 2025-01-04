from django.db import models
import numpy as np
import pandas as pd
from datetime import datetime
import random
from django.contrib.auth.forms import User
from releases.models import Release
class Profile(models.Model):
    username = models.CharField(max_length = 255 , verbose_name = "نام کاربری") 
    full_name = models.CharField(max_length = 255 , verbose_name = "نام کامل")
    email_activation_code = models.CharField(max_length = 255 , verbose_name = "کد فعالسازی ایمیل")
    related_user = models.OneToOneField(User , on_delete = models.CASCADE , verbose_name = "کاربر مرتبط")
    favorites_list = models.ManyToManyField(Release , blank = True , related_name = "favorites_list" , verbose_name = "لیست علاقه‌مندی ها")
    listening_history = models.ManyToManyField(Release , blank = True , related_name = "listening_history" , verbose_name = "تاریخچه پخش")
    @property
    def music_profile(self):
        music_profile = {
            "favorites_list" : list(self.favorites_list.all()) ,
            "listening_history" : list(self.listening_history.all()) 
        }
        return music_profile
    def __str__(self):
        return self.username
    class Meta():
        verbose_name_plural = "پروفایل ها"
        verbose_name = "پروفایل"