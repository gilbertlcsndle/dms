from django.views.generic import CreateView
from django.urls import reverse_lazy

from dms.mixins import ChairSecRequiredMixin

from .models import Attendance
from .forms import AttendanceForm

class AttendanceIndex(ChairSecRequiredMixin, CreateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = "attendance/index.html"
    success_url = reverse_lazy('attendance:index')

    def get_context_data(self, **kwargs):
        context = super(AttendanceIndex, self).get_context_data(**kwargs)
        context['object_list'] = self.model.objects.filter(
            resident__official__user__is_active = True
        )
        
        if self.request.GET.get('type') == 'residents':
            context['object_list'] = self.model.objects.filter(
                resident__status = 'act'
            ).exclude(
                resident__official__user__is_active = True
            )
        return context

