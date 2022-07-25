from django import forms
from .models import Video


class UploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'description', 'file')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input100'}),
            'description': forms.Textarea(attrs={'class': 'input100'}),
            'file': forms.FileInput(attrs={'class': 'wrap-login100-form-btn'})
        }
        # title = forms.CharField(
        #     label='Title',
        #     max_length=1000,
        #     required=True,
        #     widget=forms.TextInput(
        #         attrs={'class': 'input100'}
        #     )
        # )
