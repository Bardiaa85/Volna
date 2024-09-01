from django.db import models
from django.core.validators import FileExtensionValidator
class AboutUsText(models.Model):
    text = models.TextField()
class RulesText(models.Model):
    text = models.TextField()
class SliderShow(models.Model):
    first_image = models.ImageField(upload_to = "home")
    first_subject = models.CharField(max_length = 255)
    first_text = models.CharField(max_length = 255)
    second_image = models.ImageField(upload_to = "home")
    second_subject = models.CharField(max_length = 255)
    second_text = models.CharField(max_length = 255)
    third_image = models.ImageField(upload_to = "home")
    third_subject = models.CharField(max_length = 255)
    third_text = models.CharField(max_length = 255)
class Logo(models.Model):
    logo = models.FileField(upload_to = "home" ,  validators = [FileExtensionValidator(allowed_extensions = ['png' , 'svg'])])
class FooterInfo(models.Model):
    title = models.CharField(max_length = 255)
    text = models.CharField(max_length = 255)
    email = models.EmailField()
    telephone = models.CharField(max_length = 255)
    instagram = models.CharField(max_length = 255)
    youtube = models.CharField(max_length = 255)
    facebook = models.CharField(max_length = 255)
    twitter = models.CharField(max_length = 255)
class BrowserTabInfo(models.Model):
    text = models.CharField(max_length = 255)
    icon = models.FileField(upload_to = "home" ,  validators = [FileExtensionValidator(allowed_extensions = ['png'])])