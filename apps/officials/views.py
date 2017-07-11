from django.contrib.auth.models import User, Group
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.base import View, TemplateView, TemplateResponseMixin
from django.views.generic.edit import (
    CreateView, 
    DeleteView, 
    UpdateView, 
    FormMixin
)
from django.views.generic.list import ListView

from dms.mixins import ChairSecRequiredMixin, CalculateAgeMixin

from apps.users.forms import UserForm, SetPasswordForm, UsernameUpdateForm

from .forms import OfficialCreateForm, OfficialUpdateForm
from .models import Official

class OfficialIndex(ChairSecRequiredMixin, ListView, CalculateAgeMixin):
    model = Official
    template_name = "officials/index.html"

    def post(self, request, *args, **kwargs):
        user = User.objects.get(official__pk=request.POST['pk'])

        if user.is_active:
            user.is_active = False
        else:
            user.is_active = True

        user.save()

        return redirect('officials:index')


    def get_context_data(self, **kwargs):
        context = super(OfficialIndex, self).get_context_data(**kwargs)

        object_list = context['object_list']

        for official in object_list:
            official.age = self.get_age(official.resident.bdate)

        context['object_list'] = object_list
        return context

class OfficialCreate(ChairSecRequiredMixin, View, FormMixin, TemplateResponseMixin):
    form_class = {
        'official_form': OfficialCreateForm,
        'user_form': UserForm,
    }
    template_name = "officials/form.html"
    success_url = reverse_lazy('officials:add')

    def get_context_data(self, **kwargs):
        context = super(OfficialCreate, self).get_context_data(**kwargs)
        
        if 'form' not in kwargs:
            forms = self.get_form()
        else:
            forms = kwargs['form']

        for key in forms:
            context[key] = forms[key]

        return context

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data(**kwargs))

    def post(self, request):
        forms = self.get_form()

        # bound the forms
        bound_forms = {}
        for key in forms:
            bound_forms[key] = forms[key](request.POST, request.FILES)
        key = None

        # check if the forms are valid
        for key in bound_forms:
            if bound_forms[key].is_valid():
                forms_are_valid=True
            else:
                forms_are_valid=False
                break

        if forms_are_valid:
            return self.form_valid(form=bound_forms)
        else:
            return self.form_invalid(form=bound_forms)

    def get_form(self):
        return self.get_form_class()

    def form_valid(self, form):
        forms = form

        user = forms['user_form'].save()
        forms['official_form'].save(user.pk)

        return super(OfficialCreate, self).form_valid(form)

class OfficialUpdate(ChairSecRequiredMixin, UpdateView):
    form_class = OfficialUpdateForm
    model = Official
    template_name = "officials/form.html"
    success_url = reverse_lazy('officials:index')

    def get_context_data(self, **kwargs):
        context = super(OfficialUpdate, self).get_context_data(**kwargs)
        user = User.objects.get(official__pk=context['object'].pk)
        
        context['official_form'] = context['form']
        context['user_form'] = SetPasswordForm(user)
        context['usernameupdateform'] = UsernameUpdateForm(instance=user)
        
        context['is_edit'] = True
        
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        
        official = form.save(commit=False)

        # gets the instance of user 
        user = User.objects.get(official__pk=official.pk)

        official.save()

        usernameupdateform = UsernameUpdateForm(self.request.POST, instance=user)

        if usernameupdateform.is_valid():
            usernameupdateform.save()

            # updates the password when it's filled
            # else not
            if (
                self.request.POST.get('new_password1') and 
                self.request.POST.get('new_password2')
            ):
                user_form = SetPasswordForm(user, self.request.POST)
                
                if user_form.is_valid():
                    user_form.save()

                    return super(OfficialUpdate, self).form_valid(form)
                
                context['user_form'] = user_form
            else:
                return super(OfficialUpdate, self).form_valid(form)

        context['usernameupdateform'] = usernameupdateform

        return self.render_to_response(context)
                