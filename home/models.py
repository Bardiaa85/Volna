from django.db import models
from django.core.validators import FileExtensionValidator
class AboutUsText(models.Model):
    text = models.TextField(verbose_name = "متن")
    def __str__(self):
        return f"متن ({self.id})"
    class Meta():
        verbose_name_plural = "متن های درباره ما"
        verbose_name =  "متن درباره ما"    
class RulesText(models.Model):
    text = models.TextField(verbose_name = "متن")
    def __str__(self):
        return f"متن ({self.id})"
    class Meta():
        verbose_name_plural = "متن های قوانین و مقررات"
        verbose_name =  "متن قوانین و مقررات"  
class SliderShow(models.Model):
    first_image = models.ImageField(upload_to = "home" , verbose_name = "تصویر اول")
    first_subject = models.CharField(max_length = 255 , verbose_name = "موضوع اول")
    first_text = models.CharField(max_length = 255 , verbose_name = "متن اول")
    second_image = models.ImageField(upload_to = "home" , verbose_name = "تصویر دوم")
    second_subject = models.CharField(max_length = 255 , verbose_name = "موضوع دوم")
    second_text = models.CharField(max_length = 255 , verbose_name = "متن دوم")
    third_image = models.ImageField(upload_to = "home" , verbose_name = "تصویر سوم")
    third_subject = models.CharField(max_length = 255 , verbose_name = "موضوع سوم")
    third_text = models.CharField(max_length = 255 , verbose_name = "متن سوم")
    def __str__(self):
        return f"اسلایدرشو ({self.id})"
    class Meta():
        verbose_name_plural = "اسلایدر شو ها"
        verbose_name =  "اسلایدر شو"
class Logo(models.Model):
    logo = models.FileField(upload_to = "home" ,  validators = [FileExtensionValidator(allowed_extensions = ['png' , 'svg'])] , verbose_name = "لوگو")
    def __str__(self):
        return f"لوگو ({self.id})"
    class Meta():
        verbose_name_plural = "لوگو ها"
        verbose_name = "لوگو"
class FooterInfo(models.Model):
    title = models.CharField(max_length = 255 , verbose_name = "عنوان")
    text = models.CharField(max_length = 255 , verbose_name = "متن")
    email = models.EmailField(verbose_name = "ایمیل")
    telephone = models.CharField(max_length = 255 , verbose_name = "تلفن")
    instagram = models.CharField(max_length = 255 , verbose_name = "اینستاگرام")
    youtube = models.CharField(max_length = 255 , verbose_name = "یوتیوب")
    facebook = models.CharField(max_length = 255 , verbose_name = "فیسبوک")
    twitter = models.CharField(max_length = 255 , verbose_name = "توئیتر")
    def __str__(self):
        return f"اطلاعات ({self.id})"
    class Meta():
        verbose_name_plural = "اطلاعات فوتر"
        verbose_name = "اطلاعات"
class BrowserTabInfo(models.Model):
    text = models.CharField(max_length = 255 , verbose_name = "متن")
    icon = models.FileField(upload_to = "home" ,  validators = [FileExtensionValidator(allowed_extensions = ['png'])] , verbose_name = "لوگو")
    def __str__(self):
        return f"اطلاعات ({self.id})"
    class Meta():
        verbose_name_plural = "اطلاعات تب مرورگر"
        verbose_name = "اطلاعات"