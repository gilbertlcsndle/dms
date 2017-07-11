import datetime
from django import forms
from django.contrib.auth.models import User
from .models import Attendance

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'

    def clean(self):
        data = self.cleaned_data

        # check if the resident was already attended in the event
        is_attended = Attendance.objects.filter(
            resident = data.get('resident'), 
            date_attended = datetime.date.today(),
            event = data.get('event')
        )

        if is_attended:
            raise forms.ValidationError('You have already attended in this event.')

        return data

    