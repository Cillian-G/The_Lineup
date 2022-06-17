from django.contrib import admin

from .models import Beach
from .models import Session


@admin.register(Beach)
class BeachAdmin(admin.ModelAdmin):
    list_display = ('name', 'facing')


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('surfer', 'date', 'beach', 'time')
    list_filter = ('surfer', 'date', 'beach', 'time')
