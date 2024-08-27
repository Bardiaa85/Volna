from django.db import models
from django.contrib.auth.forms import User
class Profile(models.Model):
    username = models.CharField(max_length = 255)
    full_name = models.CharField(max_length = 255)
    email_activation_code = models.CharField(max_length = 255)
    related_user = models.OneToOneField(User , on_delete = models.CASCADE)
    def __str__(self):
        return self.username