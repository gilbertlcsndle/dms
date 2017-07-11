from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateResponseMixin
from django.urls import reverse_lazy
from django.http import JsonResponse

from dms.mixins import ChairSecRequiredMixin, CalculateAgeMixin, OfficialRequiredMixin

from .models import Resident
from .forms import ResidentForm

class ResidentIndex(OfficialRequiredMixin, ListView, CalculateAgeMixin):
    model = Resident
    template_name = "residents/index.html"

    def get_context_data(self, **kwargs):
        context = super(ResidentIndex, self).get_context_data(**kwargs)

        object_list = context['object_list']

        for resident in object_list:
            resident.age = self.get_age(resident.bdate)

        context['object_list'] = object_list
        return context

class ResidentCreate(ChairSecRequiredMixin, CreateView):
    form_class = ResidentForm
    template_name = "residents/form.html"
    success_url = reverse_lazy('residents:add')

class ResidentUpdate(ChairSecRequiredMixin, UpdateView):
    form_class = ResidentForm
    model = Resident
    template_name = "residents/form.html"
    success_url = reverse_lazy('residents:index')

    def get_context_data(self, **kwargs):
        context = super(ResidentUpdate, self).get_context_data(**kwargs)
        context['is_edit'] = True
        return context

class ResidentDetail(OfficialRequiredMixin, DetailView, CalculateAgeMixin):
    model = Resident
    template_name = "residents/view2.html"

    def get_context_data(self, **kwargs):
        context = super(ResidentDetail, self).get_context_data(**kwargs)
        context['object'].age = self.get_age(context['object'].bdate)
        return context

# ajax 

def get_resident_names(request):
    all_residents = Resident.objects.all()

    resident_names = []

    for resident in all_residents:
        name = '%s %s %s' %(resident.fname, resident.mname, resident.lname)

        if 'q' in request.GET and len(request.GET['q']):
            if request.GET['q'].lower() in name.lower(): 
                resident_names.append({
                    'resident_pk': str(resident.pk),
                    'resident': name,
                })

    return JsonResponse(resident_names, safe=False)