from django import forms
from django.forms import ModelForm
from accounts.models import UserInfo

class UserInfoUpdateForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['firstname','lastname','username','phone','email']