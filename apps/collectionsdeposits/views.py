from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponse
from django.db.models import Sum

from dms.mixins import TreasureRequiredMixin

from apps.residents.models import Resident

from .forms import CollectionForm
from .models import Collection, Particular

def get_collection_context():
    context = {}
    context['object_list'] = Collection.objects.all()
    context['all_particulars'] = Particular.objects.all()
    
    context['total'] = 0
    
    total = Collection.objects.aggregate(Sum('collection'))

    if total['collection__sum']:
        context['total'] = total['collection__sum']

    return context

class CollectionIndex(TreasureRequiredMixin, CreateView):
    form_class = CollectionForm
    template_name = "collectionsdeposits/index.html"
    success_url = reverse_lazy('collectionsdeposits:index')

    def get_context_data(self, **kwargs):
        context = super(CollectionIndex, self).get_context_data(**kwargs)
        context.update(get_collection_context())
        return context  

class CollectionPrint(TemplateView):
    template_name = "collectionsdeposits/print-table.html"

    def get_context_data(self, **kwargs):
        context = super(CollectionPrint, self).get_context_data(**kwargs)
        context['object_list'] = Collection.objects.all()

        return context

class CollectionUpdate(TreasureRequiredMixin, UpdateView):
    model = Collection
    form_class = CollectionForm
    success_url = reverse_lazy('collectionsdeposits:index')
    template_name = "collectionsdeposits/index.html"

    def get_context_data(self, **kwargs):
        context = super(CollectionUpdate, self).get_context_data(**kwargs)
        context.update(get_collection_context())
        context['is_edit'] = True
        return context

class ParticularIndex(TreasureRequiredMixin, CreateView):
    model = Particular
    template_name = "particulars/index.html"
    fields = '__all__'
    success_url = reverse_lazy('collectionsdeposits:particulars')

    def get_context_data(self, **kwargs):
        context = super(ParticularIndex, self).get_context_data(**kwargs)
        context['object_list'] = self.model.objects.all()

        return context

def get_particular_amount(request):
    particular = Particular.objects.get(pk=request.GET.get('pk'))

    return HttpResponse(particular.amount)

class ParticularUpdate(TreasureRequiredMixin, UpdateView):
    model = Particular
    template_name = "particulars/index.html"
    fields = '__all__'
    success_url = reverse_lazy('collectionsdeposits:particulars')

    def get_context_data(self, **kwargs):
        context = super(ParticularUpdate, self).get_context_data(**kwargs)
        context['object_list'] = self.model.objects.all()
        context['is_edit'] = True
        return context

class ParticularDelete(TreasureRequiredMixin, DeleteView):
    model = Particular
    success_url = reverse_lazy('collectionsdeposits:particulars')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)