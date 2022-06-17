import datetime
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Beach, Session
from .forms import SessionForm


class BeachList(generic.ListView):
    model = Beach
    queryset = Beach.objects.order_by("name")
    template_name = "index.html"


today = datetime.datetime.now()
tomorrow = today + datetime.timedelta(days=1)
day_after_tomorrow = today + datetime.timedelta(days=2)


class BeachSessions(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Beach
        beach = get_object_or_404(queryset, slug=slug)
        sessions = beach.sessions.filter(
            date__gte=today, date__lte=day_after_tomorrow).order_by(
                "date", "time")
        return render(
            request,
            "beach_sessions.html",
            {
                "beach": beach,
                "sessions": sessions,
                "session_form": SessionForm(),
                "today": today,
                "tomorrow": tomorrow,
                "day_after_tomorrow": day_after_tomorrow,
            }
         )

    def post(self, request, slug, *args, **kwargs):
        queryset = Beach
        beach = get_object_or_404(queryset, slug=slug)
        sessions = beach.sessions.filter(
            date__gte=today, date__lte=day_after_tomorrow).order_by(
                "date", "time")

        session_form = SessionForm(data=request.POST)

        if session_form.is_valid():
            session_form.instance.surfer = request.user
            session = session_form.save(commit=False)
            session.beach = beach
            session.save()
        else:
            session_form = SessionForm()

        return render(
            request,
            "beach_sessions.html",
            {
                "beach": beach,
                "sessions": sessions,
                "session_form": SessionForm(),
                "today": today,
                "tomorrow": tomorrow,
                "day_after_tomorrow": day_after_tomorrow,
            }
         )
