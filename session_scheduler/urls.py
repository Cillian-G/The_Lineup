from . import views
from django.urls import path

urlpatterns = [
    path('', views.BeachList.as_view(), name='home'),
    path('<slug:slug>/', views.BeachSessions.as_view(), name='beach_sessions'),
]