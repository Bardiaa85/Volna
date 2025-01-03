from django.db import models
from django.utils import timezone
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
class Article(models.Model):
    title = models.CharField(max_length = 255 , verbose_name = "عنوان")
    article_date = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(verbose_name = "پیوندک")
    image = models.ImageField(upload_to = "news" , verbose_name = "تصویر")
    content = models.TextField(verbose_name = "محتوا")
    def get_time(self):
        formatted_time = self.article_date.strftime("%I:%M%p")
        formatted_time = formatted_time.replace("PM" , " بعد از ظهر ").replace("AM" , " قبل از ظهر")
        return formatted_time
    def get_solar_date(self):
        jdate = jdatetime.date.fromgregorian(date = self.article_date)
        jdate_hmonth = persian_months[jdate.month]
        jdate = jdate.strftime(f"%d {jdate_hmonth} %Y")
        return jdate
    def time_since(self):
        now = timezone.now()
        diff = now - self.article_date
        seconds = diff.total_seconds()
        minutes = seconds // 60
        hours = minutes // 60
        days = hours // 24
        weeks = days // 7
        months = days // 30
        years = days // 365
        if seconds < 60 :
            return f"{int(seconds)} ثانیه پیش"
        elif minutes < 60 :
            return f"{int(minutes)} دقیقه پیش"
        elif hours < 24 :
            return f"{int(hours)} ساعت پیش"
        elif days < 7 :
            return f"{int(days)} روز پیش"
        elif weeks < 4 :
            return f"{int(weeks)} هفته پیش"
        elif months < 12 :
            return f"{int(months)} ماه پیش"
        else:
            return f"{int(years)} سال پیش"
    def len_comments(self):
        return len(self.comment_set.all())
    def __str__(self):
        return self.title
    class Meta() :
        verbose_name = "مقاله"
        verbose_name_plural = "اخبار"