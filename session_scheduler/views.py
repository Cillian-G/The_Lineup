from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Beach, Session

class BeachList(generic.ListView):
    model = Beach
    queryset = Beach.objects.order_by("name")
    template_name = "index.html"

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
            },
         )
