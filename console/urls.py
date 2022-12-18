from django.urls import include, path

from console.views import Dashboard, MakeAppointment, MakePaymentView, Sessions

app_name = 'console'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('appointment', MakeAppointment.as_view(), name='appointment'),
    path('payment', MakePaymentView.as_view(), name='payment'),
    path('payment/<int:appointment_id>', MakePaymentView.as_view(), name='payment'),
    path('sessions', Sessions.as_view(), name='sessions'),
]
