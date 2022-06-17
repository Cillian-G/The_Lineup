from . import views
from django.urls import path
from session_scheduler.views import edit_session, delete_session

urlpatterns = [
    path('', views.BeachList.as_view(), name='home'),
    path('<slug:slug>/', views.BeachSessions.as_view(), name='beach_sessions'),
    path('edit/<item_id>', edit_session, name='edit'),
    path('delete/<item_id>', delete_session, name='delete'),
]
