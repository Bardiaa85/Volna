from django.db import models
from artists.models import Artist
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
class Event(models.Model):
    title = models.CharField(max_length = 255 , verbose_name = "عنوان")
    description = models.CharField(max_length = 255 , verbose_name = "توضیحات")
    content = models.TextField(verbose_name = "محتوا")
    in_progress = models.BooleanField(default = True , verbose_name = "در حال جریان")
    slug = models.SlugField(verbose_name = "پیوندک")
    related_artist = models.ForeignKey(Artist , on_delete = models.CASCADE , null = True , blank = True , verbose_name = "هنرمند مرتبط")
    image = models.ImageField(upload_to = "events" , verbose_name = "تصویر")
    event_date = models.DateTimeField(verbose_name = "تاریخ رویداد")
    def get_time(self):
        formatted_time = self.event_date.strftime("%I:%M%p")
        formatted_time = formatted_time.replace("PM" , " بعد از ظهر ").replace("AM" , " قبل از ظهر")
        return formatted_time
    def get_solar_date(self):
        jdate = jdatetime.date.fromgregorian(date = self.event_date)
        jdate_hmonth = persian_months[jdate.month]
        jdate = jdate.strftime(f"%d {jdate_hmonth} %Y")
        return jdate
    def __str__(self):
        return self.title
    class Meta():
        verbose_name_plural = "رویداد ها"
        verbose_name = "رویداد"