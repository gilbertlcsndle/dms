from django import forms
from .models import Resident

class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = '__all__'
        widgets = {
            'gender': forms.RadioSelect(),
            'educational_attainment': forms.RadioSelect(),
            'status': forms.RadioSelect(),
        }
