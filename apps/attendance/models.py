from django.db import models
from apps.residents.models import Resident
from apps.events.models import Event

class Attendance(models.Model):
    resident = models.ForeignKey(Resident, verbose_name='attendee')
    date_attended = models.DateField(auto_now_add=True)
    time_attended = models.TimeField(auto_now_add=True)
    event = models.ForeignKey(Event)

    def __str__(self):
        return '{0} {1}'.format(self.resident.fname, self.resident.lname)
    