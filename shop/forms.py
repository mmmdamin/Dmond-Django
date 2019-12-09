from django import forms

from shop.models import Member, Product


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
        fields = ['username', 'email', 'password']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "price", "deactivated")