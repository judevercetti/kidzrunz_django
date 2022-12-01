from django.urls import include, path

from console.views import Dashboard

app_name = 'console'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
]
