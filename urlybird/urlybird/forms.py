from django import forms
from django.contrib.auth.models import User
# from bookmarks.models import Worm


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

# class WormForm(forms.ModelForm):
#     class Meta:
#         model = Worm
#         fields = ['worm']
