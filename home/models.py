from django.db import models
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
