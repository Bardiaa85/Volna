from django.db import models
from django.contrib.auth.forms import User
from releases.models import Release
class Profile(models.Model):
    username = models.CharField(max_length = 255)
    full_name = models.CharField(max_length = 255)
    email_activation_code = models.CharField(max_length = 255)
    related_user = models.OneToOneField(User , on_delete = models.CASCADE)
    favorites_list = models.ManyToManyField(Release , blank = True , related_name = "favorites_list")
    def __str__(self):
        return self.username