from django.urls import include, path

from console.views import AdminHomeView, Dashboard, MakeAppointment, MakePaymentView, ProfileView, ReportsView, SessionsView, TransactionsView

app_name = 'console'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('appointment', MakeAppointment.as_view(), name='appointment'),
    path('payment', MakePaymentView.as_view(), name='payment'),
    path('payment/<int:appointment_id>', MakePaymentView.as_view(), name='payment'),
    path('home', AdminHomeView.as_view(), name='home'),
    path('sessions', SessionsView.as_view(), name='sessions'),
    path('reports', ReportsView.as_view(), name='reports'),
    path('transactions', TransactionsView.as_view(), name='transactions'),
]
