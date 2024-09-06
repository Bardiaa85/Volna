from django.db import models
from news.models import Article
from releases.models import Release
from account.models import Profile
from django.contrib.auth.forms import User
import jdatetime
persian_months = {
    1 : "فروردین" , 
    2 : "اردیبهشت" ,
    3 : "خرداد" ,
    4 : "تیر" ,
    5 : "مرداد" ,
    6 : "شهریور" ,
    7 : "مهر" ,
    8 : "آبان" ,
    9 : "آذر" ,
    10 : "دی" ,
    11 : "بهمن" ,
    12 : "اسفند" 
}
class Comment(models.Model):
    content = models.CharField(max_length = 255 , verbose_name = "محتوا")
    comment_date = models.DateTimeField(auto_now_add = True)
    related_user = models.ForeignKey(User , on_delete = models.CASCADE , verbose_name = "کاربر مرتبط")
    related_release = models.ForeignKey(Release , on_delete = models.CASCADE , null = True , blank = True , verbose_name = "موزیک مرتبط")
    related_article = models.ForeignKey(Article , on_delete = models.CASCADE , null = True , blank = True , verbose_name = "مقاله مرتبط")
    def related_profile(self):
        return Profile.objects.get(related_user = self.related_user)
    def get_time(self):
        formatted_time = self.comment_date.strftime("%I:%M%p")
        formatted_time = formatted_time.replace("PM" , " بعد از ظهر ").replace("AM" , " قبل از ظهر")
        return formatted_time
    def get_solar_date(self):
        jdate = jdatetime.date.fromgregorian(date = self.comment_date)
        jdate_hmonth = persian_months[jdate.month]
        jdate = jdate.strftime(f"%d {jdate_hmonth} %Y")
        return jdate
    def __str__(self):
        return self.content   
    class Meta():
        verbose_name_plural = "کامنت ها"
        verbose_name = "کامنت"