from django.contrib import admin

from .models import Beach
from .models import Session
# Register your models here.

admin.site.register(Beach)
admin.site.register(Session)