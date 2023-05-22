from django import forms
from .models import Profile
from core.account.forms import SignUpForm


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    
    
    class SignUpForm(forms.ModelForm):
        class Meta:
            model = Profile
            fields = ('username', 'email', 'first_name', 'last_name', 'password','address','phone_number')
            exclude =('is_verified', 'is_admin', 'is_staff', 'is_seller')