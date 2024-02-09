
from django import forms
from django.contrib.auth.models import User

from user_app.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name' ,'last_name','email']


