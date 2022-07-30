from django import forms
from .models import User


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input100'}),
            'password': forms.TextInput(attrs={'class': 'input100'}),
        }
