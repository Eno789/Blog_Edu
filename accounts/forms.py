from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import User

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email_url'].required = True
        self.fields['phone_number'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if phone:
            qs = User.objects.filter(phone_number=phone)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 핸드폰 번호입니다.")
        return phone
    def clean_email_url(self):
        email_url = self.cleaned_data.get('email_url')
        if email_url:
            qs = User.objects.filter(email_url=email_url)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 이메일 주소입니다.")
        return email_url

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'email_url']