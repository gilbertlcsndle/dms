from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse

from dms.mixins import ChairSecRequiredMixin

from .forms import EventForm
from .models import Event

class EventIndex(ChairSecRequiredMixin, CreateView):
    form_class = EventForm
    model = Event
    template_name = "events/index.html"
    success_url = reverse_lazy('events:index')

    def get_context_data(self, **kwargs):
        context = super(EventIndex, self).get_context_data(**kwargs)
        context['object_list'] = self.model.objects.all()
        return context

class EventUpdate(ChairSecRequiredMixin, UpdateView):
    form_class = EventForm
    model = Event
    template_name = "events/index.html"
    success_url = reverse_lazy('events:index')

    def get_context_data(self, **kwargs):
        context = super(EventUpdate, self).get_context_data(**kwargs)
        context['object_list'] = self.model.objects.all()
        context['is_edit'] = True

        return context

class EventDelete(ChairSecRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('events:index')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class EventDetail(View):
    def get(self, request, *args, **kwargs):
        event = Event.objects.get(pk=request.GET.get('pk'))
        data = {
            'title': event.title,
            'description': event.description,
            'start': event.start,
            'end': event.end,
        }

        return JsonResponse(data, safe=False)
