from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm, 
    SetPasswordForm
)
from django import forms

class UserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = 'Id no'
        self.fields['username'].widget.attrs.pop("autofocus", None)

        # removes help texts
        for fieldname in self.fields:
            self.fields[fieldname].help_text = None

class SetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(SetPasswordForm, self).__init__(*args, **kwargs)

        self.fields['new_password1'].help_text = None
        self.fields['new_password1'].required = False
        self.fields['new_password2'].required = False

class UsernameUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super(UsernameUpdateForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = 'Id no'
        self.fields['username'].help_text = None
    