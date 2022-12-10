from django.urls import include, path

from console.views import Dashboard, Sessions

app_name = 'console'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('sessions', Sessions.as_view(), name='sessions'),
]
