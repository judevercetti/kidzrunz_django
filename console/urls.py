from django.urls import include, path

from console.views import *

app_name = 'console'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('appointment', MakeAppointment.as_view(), name='appointment'),
    # path('payment', trialll, name='payment'),
    path('payment/success', payment_success, name='payment-success'),
    path('payment/cancel', payment_cancel, name='payment-cancel'),
    path('payment/<int:appointment_id>',
         MakePaymentView.as_view(), name='payment'),
    path('home', AdminHomeView.as_view(), name='home'),
    path('sessions', SessionsView.as_view(), name='sessions'),
    path('reports', ReportsView.as_view(), name='reports'),
    path('transactions', TransactionsView.as_view(), name='transactions'),
]
