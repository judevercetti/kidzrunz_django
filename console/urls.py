from django.urls import include, path

from console.views import Dashboard, MakeAppointment, Sessions

app_name = 'console'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('appointment', MakeAppointment.as_view(), name='appointment'),
    path('sessions', Sessions.as_view(), name='sessions'),
]
