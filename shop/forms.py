from django import forms
from django.core.exceptions import ValidationError

from shop.models import Member


class SignInForm(forms.ModelForm):
    class Meta:
        model = Member
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['username', 'password']


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Member
        fields = ['username', 'email', 'image', 'password', 'image']

    def clean_password1(self):
        raise ValidationError('x')
