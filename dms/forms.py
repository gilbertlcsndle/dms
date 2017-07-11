from django import forms
from django.contrib.auth.forms import AuthenticationForm
from apps.files.models import File

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'
        widgets = {
            'file': forms.ClearableFileInput(attrs={'multiple': True}),
        }

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = 'Id no'
