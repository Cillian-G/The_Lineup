from django.contrib import admin

from .models import Beach
from .models import Session
# Register your models here.

@admin.register(Beach)
class BeachAdmin(admin.ModelAdmin):
    list_display = ('name', 'facing')
    # add filter for choice of facing

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('surfer', 'date','beach', 'time')
    list_filter = ('surfer', 'date','beach', 'time')

