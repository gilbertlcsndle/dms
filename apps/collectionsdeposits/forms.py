from django import forms

from apps.residents.models import Resident

from .models import Collection

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = '__all__'
        widgets = {
            'collection': forms.HiddenInput(),
        }


# form with saving balance
# class CollectionForm(forms.ModelForm):
#     class Meta:
#         model = Collection
#         exclude = ('balance',)
        

#     def save(self, commit=True):
#         collection = super(CollectionForm, self).save(commit=False)

#         total = Collection.objects.aggregate(Sum('collection'))

#         # put the current total in balance
#         if total['collection__sum'] is None:
#             collection.balance = 0
#         else: 
#             collection.balance = total['collection__sum']

#         if commit:
#             collection.save()

#         return collection
    