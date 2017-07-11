from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponse
from django.views.generic.base import TemplateView, View, RedirectView
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render
from django.db.models import Sum

from apps.events.models import Event
from apps.residents.models import Resident
from apps.officials.models import Official
from apps.collectionsdeposits.models import Collection
from apps.files.models import File

from .mixins import ChairSecRequiredMixin, OfficialRequiredMixin
from .forms import FileForm

class Index(RedirectView):
    pattern_name = 'login'

class Dashboard(OfficialRequiredMixin, TemplateView):
    template_name = 'admin/dashboard.html'

    def get_context_data(self, **kwargs):
        collection = Collection.objects.aggregate(Sum('collection'))

        context = super(Dashboard, self).get_context_data(**kwargs)
        context['file_form'] = FileForm
        context['object_list'] = File.objects.all()
        context['total_residents'] = Resident.objects.filter(status='act').count()
        
        if collection['collection__sum'] is not None:
            context['total_collections'] = collection['collection__sum']
        else:
            context['total_collections'] = 0
        
        return context

class FileCreate(ChairSecRequiredMixin, FormView):
    form_class = FileForm

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file')

        if form.is_valid():
            for f in files:
                File.objects.create(file=f)
            return JsonResponse({}, safe=False)
        else:
            return JsonResponse({}, safe=False)

class FileDelete(ChairSecRequiredMixin, DeleteView):
    model = File
    success_url = reverse_lazy('dashboard')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class EventList(View):
    def get(self, request, *args, **kwargs):
        all_events = Event.objects.all()
        event_list = []

        for event in all_events:
            event_list.append({
                'pk': event.pk,
                'title': event.title,
                'description': event.description,
                'start': event.start,
                'end': event.end
            })
            
        return JsonResponse(event_list, safe=False)
    

