from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Beach, Session
import datetime

class BeachList(generic.ListView):
    model = Beach
    queryset = Beach.objects.order_by("name")
    template_name = "index.html"


date = datetime.datetime.now()
todays_year = date.strftime("%Y")
todays_month = date.strftime("%B")
todays_day = date.strftime("%d")
todays_full_date = f"{todays_month} {todays_day}, {todays_year}"


class BeachSessions(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Beach
        beach = get_object_or_404(queryset, slug=slug)
        sessions = beach.sessions.order_by("time")



        return render(
            request,
            "beach_sessions.html",
            {
                "beach": beach,
                "sessions": sessions,
                "todays_full_date": todays_full_date 
            },
         )
