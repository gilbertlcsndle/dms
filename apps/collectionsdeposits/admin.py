from django.contrib import admin
from .models import Collection, Particular

class CollectionAdmin(admin.ModelAdmin):
    list_display = [
        'date',
        'payor',
        'particular',
        'collection',
    ]

class ParticularAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'amount',
    ]

admin.site.register(Collection, CollectionAdmin)
admin.site.register(Particular, ParticularAdmin)