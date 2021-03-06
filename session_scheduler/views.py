import datetime
from django.shortcuts import render, get_object_or_404, redirect
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


def edit_session(request, item_id):

    session = get_object_or_404(Session, id=item_id)
    beach = session.beach
    slug = beach.slug

    if request.method == "POST":
        session_form = SessionForm(request.POST, instance=session)
        if session_form.is_valid():
            session_form.instance.surfer = request.user
            session = session_form.save(commit=False)
            session.save()
            return redirect('beach_sessions', slug=slug)
    context = {
        'session_form': SessionForm(),
        'beach': beach
    }
    return render(request, "edit_session.html", context)


def delete_session(request, item_id):
    session = get_object_or_404(Session, id=item_id)
    beach = session.beach
    slug = beach.slug
    username = session.surfer
    time = session.time
    date = session.date
    if request.method == 'POST':
        session.delete()
        return redirect('beach_sessions', slug=slug)
    context = {
        'session': session,
        'username': username,
        'beach': beach,
        'time': time,
        'date': date,
    }
    return render(request, 'delete_session.html', context)
