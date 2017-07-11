from django.contrib import admin
from .models import Resident

class ResidentAdmin(admin.ModelAdmin):
    list_display = [
        'fname',
        'mname',
        'lname',
        'gender',
        'bdate',
        'address',
        'civil_status',
        'occupation',
        'educational_attainment',
        'spouse',
    ]

admin.site.register(Resident, ResidentAdmin)
