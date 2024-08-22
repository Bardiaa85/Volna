from django import forms
from .models import ContactUsMessage
class ContactUsMessageModelForm(forms.ModelForm):
    class Meta :
        model = ContactUsMessage
        fields = ["name" , "email" , "subject" , "text"]
        labels = {"name" : "" , "email" : "" , "subject" : "" , "text" : ""}
        widgets = {
            "name" : forms.TextInput(attrs = {"placeholder" : "نام" , "class" : "sign__input"}),
            "email" : forms.TextInput(attrs = {"placeholder" : "ایمیل" , "class" : "sign__input"}),
            "subject" : forms.TextInput(attrs = {"placeholder" : "موضوع" , "class" : "sign__input"}),
            "text" : forms.Textarea(attrs = {"placeholder" : "پیام خود را بنویسید . . ." , "class" : "sign__textarea"})
        }
        error_messages = {
            "name" : {"required" : "پر کردن این فیلد اجباری می باشد"},
            "email" : {"required" : "پر کردن این فیلد اجباری می باشد" , "invalid" : "لطفاً ایمیل خود را درست وارد کنید"},
            "subject" : {"required" : "پر کردن این فیلد اجباری می باشد"},
            "text" : {"required" : "پر کردن این فیلد اجباری می باشد"}
        }