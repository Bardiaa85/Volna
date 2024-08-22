from django.db import models
class ContactUsMessage(models.Model):
    subject = models.CharField(max_length = 120)
    name = models.CharField(max_length =120)
    email = models.EmailField()
    text = models.TextField()
    admin_response = models.TextField(null = True, blank = True)
    is_read_by_admin = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.subject
