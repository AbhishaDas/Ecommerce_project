from django import forms
from accounts.models import UserInfo

class UserInfoUpdateForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['first_name', 'last_name', 'email', 'phone']