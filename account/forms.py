from django import forms
from django.core.exceptions import ValidationError
class SignUpForm(forms.Form):
    full_name = forms.CharField(required = True , max_length = 255 , widget = forms.TextInput(attrs = {"placeholder" : "نام و نام خانوادگی" , "class" : "sign__input"}) , error_messages = {"required" : "پر کردن این فیلد الزامی است"})
    email = forms.EmailField(required = True , max_length = 255 , widget = forms.EmailInput(attrs = {"placeholder" : "ایمیل" , "class" : "sign__input"})  , error_messages = {"required" : "پر کردن این فیلد الزامی است" , "invalid" : "ایمیل وارد شده معتبر نیست"})
    password = forms.CharField(required = True , max_length = 255 , widget = forms.PasswordInput(attrs = {"placeholder" : "رمز عبور" , "class" : "sign__input"})  , error_messages = {"required" : "پر کردن این فیلد الزامی است"})
    password_confirmation = forms.CharField(required = True , max_length = 255 , widget = forms.PasswordInput(attrs = {"placeholder" : "تایید رمز عبور" , "class" : "sign__input"})  , error_messages = {"required" : "پر کردن این فیلد الزامی است"})
    def clean_password_confirmation(self):
        password = self.cleaned_data.get("password")
        password_confirmation = self.cleaned_data.get("password_confirmation")
        if password != password_confirmation:
            raise ValidationError("رمز عبور و تایید آن باهم مطابقت ندارند")
        else:
            return password_confirmation
class SignInForm(forms.Form):
    email = forms.EmailField(required = True , max_length = 255 , widget = forms.EmailInput(attrs = {"placeholder" : "ایمیل" , "class" : "sign__input"})  , error_messages = {"required" : "پر کردن این فیلد الزامی است" , "invalid" : "ایمیل وارد شده معتبر نیست"})
    password = password = forms.CharField(required = True , max_length = 255 , widget = forms.PasswordInput(attrs = {"placeholder" : "رمز عبور" , "class" : "sign__input"})  , error_messages = {"required" : "پر کردن این فیلد الزامی است"})