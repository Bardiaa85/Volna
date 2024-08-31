from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import ContactUsMessage
@receiver(post_save , sender = ContactUsMessage)
def handle_admin_response(sender , instance , **kwargs):
    if instance.admin_response and instance.is_read_by_admin :
        html_message = render_to_string("email_templates/admin-response.html" , context = {"user_message" : instance.text , "admin_message" : instance.admin_response}) 
        plain_message = strip_tags(html_message)  
        send_mail(
            subject = instance.subject ,
            from_email = settings.EMAIL_HOST_USER ,
            recipient_list = [instance.email] ,
            message = plain_message ,
            html_message = html_message
            ) 
    
