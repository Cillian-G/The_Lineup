from django.shortcuts import render
from django.views import generic
from .models import Beach, Session

class BeachList(generic.ListView):
    model = Beach
    queryset = Beach.objects.order_by("name")
    template_name = "index.html"


