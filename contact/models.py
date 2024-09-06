from django.db import models
class ContactUsMessage(models.Model):
    subject = models.CharField(max_length = 120 , verbose_name = "موضوع")
    name = models.CharField(max_length = 120 , verbose_name = "نام")
    email = models.EmailField(verbose_name = "ایمیل")
    text = models.TextField(verbose_name = "متن")
    admin_response = models.TextField(null = True, blank = True , verbose_name = "پاسخ ادمین")
    is_read_by_admin = models.BooleanField(default = False , verbose_name = "خوانده شده توسط ادمین")
    created = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.subject
    class Meta():
        verbose_name_plural = "پبام های تماس با ما"
        verbose_name = "پیام تماس با ما"