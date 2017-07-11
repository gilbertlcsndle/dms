from django.contrib import admin
from .models import Official

class OfficialAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'resident',
        'position'
    ]

admin.site.register(Official, OfficialAdmin)