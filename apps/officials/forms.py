from django.contrib.auth.models import User
from django import forms
from dms.mixins import position_keys
from apps.residents.models import Resident
from .models import Official

class OfficialCreateForm(forms.ModelForm):
    class Meta:
        model = Official
        exclude = ('user',)
        widgets = {
            'position': forms.RadioSelect(),
        }

    def save(self, user_pk, commit=True):
        official = super(OfficialCreateForm, self).save(commit=False)
        official.user = User.objects.get(pk=user_pk)

        if self.cleaned_data.get('position') in position_keys[:2]:
            official.user.is_superuser = True
            official.user.is_staff = True

        if commit:
            official.save()          

        return official

class OfficialUpdateForm(forms.ModelForm):
    class Meta:
        model = Official
        exclude = ('user',)
        widgets = {
            'position': forms.RadioSelect(),
        }

    def save(self, commit=True):
        official = super(OfficialUpdateForm, self).save(commit=False)

        user = User.objects.get(official__pk=official.pk)
        
        if self.cleaned_data.get('position') in position_keys[:2]:
            user.is_superuser = True
            user.is_staff = True
        else:
            # set to false if position was change from chairman or secretary
            user.is_superuser = False
            user.is_staff = False

        if commit:
            official.save()
            user.save()

        return official