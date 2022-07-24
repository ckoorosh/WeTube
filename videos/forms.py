from django import forms


class UploadForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        max_length=1000,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'input100'}
        )
    )
