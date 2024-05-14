import braintree
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.db.models import Sum
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
import stripe
from auth_app.models import Profile, User
from console.forms import AppointmentForm
from console.models import Appointment, BraintreeCustomer, BraintreeTransaction

from website.models import Package

# Create your views here.


class Dashboard(LoginRequiredMixin, View):
    login_url = 'login'
    template_name = "console/user/dashboard.html"

    def get(self, request):
        appointments = Appointment.objects.filter(
            user=request.user).order_by('-created_on')
        context = {'appointments': appointments}
        return render(request, self.template_name, context=context)

    def post(self, request):
        appointment = Appointment.objects.get(
            pk=request.POST.get('appointment_id'))
        appointment.status = Appointment.Status.CANCELLED
        appointment.save()
        return redirect('console:dashboard')


class ProfileView(View):
    template_name = "console/user/profile.html"

    def get(self, request):
        context = {'genders': Profile.Gender.choices}
        return render(request, self.template_name, context)

    def post(self, request):
        user = User.objects.get(pk=request.user.id)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.phone_number = request.POST.get('phone_number')
        user.email = request.POST.get('email')
        user.profile.gender = request.POST.get('gender')
        user.profile.street_address = request.POST.get('street_address')
        user.profile.city = request.POST.get('city')
        user.profile.state = request.POST.get('state')
        user.profile.postal_code = request.POST.get('postal_code')
        print(request.FILES.get('display_photo'))
        if request.FILES.get('display_photo'):
            user.display_photo = request.FILES.get('display_photo')

        user.save()
        return redirect('console:profile')


class MakeAppointment(LoginRequiredMixin, View):
    login_url = 'login'
    template_name = "console/user/make_appointment.html"

    def get(self, request):
        packages = Package.objects.all()
        context = {'packages': packages}
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = AppointmentForm(request.POST)

        if form.is_valid():
            print('valid')
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()

            return redirect("console:dashboard")
        else:
            print(form.errors)
            print('invalid')
            return redirect('console:appointment')


def trialll(request):
    stripe.api_key = 'sk_test_51NjQ5oE0Ojdo2alyEWyFGPhY3ejC28kvzxv9K6RT0PGIGtMiNA6AP8HWWp59NE8Ky8LH9NbwEWkZ6ZDtiz3fJbrs00mkIIBs8o'
    # return HttpResponse('trialxxxxx')

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1NjeydE0Ojdo2aly37UoKCqD',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://localhost:8000/console/payment/success',
            cancel_url='http://localhost:8000/console/payment/cancel',
        )
    except Exception as e:
        print(f'error: {e}')
        return HttpResponse('error') #str(e)

    return redirect(checkout_session.url, code=303)

def payment_success(request):
    context = {}
    return render(request, 'console/user/payment_success.html', context=context)

def payment_cancel(request):
    context = {}
    return render(request, 'console/user/payment_cancel.html', context=context)

class MakeStripePaymentView(LoginRequiredMixin, View):
    login_url = 'login'
    template_name = "console/user/make_payment.html"
    # stripe.api_key = 'sk_test_51NjQ5oE0Ojdo2alyEWyFGPhY3ejC28kvzxv9K6RT0PGIGtMiNA6AP8HWWp59NE8Ky8LH9NbwEWkZ6ZDtiz3fJbrs00mkIIBs8o'

    def get(self, request, appointment_id=None):
        return 'oi'
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': '5',
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url='/payment/success',
                cancel_url='/payment/cancel',
            )
        except Exception as e:
            return str(e)

        return redirect(checkout_session.url, code=303)


class MakePaymentView(LoginRequiredMixin, View):
    login_url = 'login'
    template_name = "console/user/make_payment.html"

    gateway = braintree.BraintreeGateway(
        braintree.Configuration(
            braintree.Environment.Sandbox,
            merchant_id="x536wfbzjdzxqn5p",
            public_key="t67qzgcjpyx4rntg",
            private_key="4c383ddde0682fac2e5f46c2cfff4c6a"
        )
    )

    def get(self, request, appointment_id):

        try:
            customer_id = BraintreeCustomer.objects.get(
                user=request.user).customer_id
        except:
            result = self.gateway.customer.create({
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "email": request.user.email,
                "phone": request.user.phone_number,
            })
            if result.is_success:
                new_customer = result.customer

            customer_id = BraintreeCustomer.objects.create(
                user=request.user, customer_id=new_customer.id).customer_id

        client_token = self.gateway.client_token.generate({
            "customer_id": customer_id
        })

        amount = Appointment.objects.get(pk=appointment_id).package.price

        context = {
            'client_token': client_token,
            'appointment_id': appointment_id,
            'amount': amount
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        nonce_from_the_client = request.POST.get("payment_method_nonce")
        appointment_id = request.POST.get("appointment_id")
        amount = Appointment.objects.get(pk=appointment_id).package.price
        print(nonce_from_the_client)

        result = self.gateway.transaction.sale({
            "amount": amount,
            "payment_method_nonce": nonce_from_the_client,
            # "device_data": device_data_from_the_client,
            "options": {
                "submit_for_settlement": True
            }
        })

        success = False

        # Check if the transaction was successful
        if result.is_success:
            print("Transaction successful!")
            transaction = BraintreeTransaction.objects.create(
                appointment_id=appointment_id, transaction_id=result.transaction.id)
            if not transaction:
                print('transaction was not saved to db')
            success = True
        else:
            print("Transaction failed:")
            for error in result.errors.deep_errors:
                print(error.code, error.message)

        return JsonResponse({'success': success})


class AdminHomeView(LoginRequiredMixin, View):
    template_name = "console/admin/dashboard.html"

    def get(self, request):
        appointments = Appointment.objects.filter(status=Appointment.Status.APPROVED)
        total_clients = User.objects.count()
        total_sessions = Appointment.objects.count()
        active_sessions = Appointment.objects.filter(status=Appointment.Status.APPROVED).count()
        total_amount = BraintreeTransaction.objects.aggregate(
            amount=Sum('amount'))['amount']
        context = {
            'appointments': appointments,
            'total_clients': total_clients,
            'total_sessions': total_sessions,
            'active_sessions': active_sessions,
            'total_amount': total_amount,
        }
        return render(request, self.template_name, context=context)


class SessionsView(LoginRequiredMixin, View):
    template_name = "console/admin/sessions.html"

    def get(self, request):
        appointments = Appointment.objects.all()
        context = {'appointments': appointments}
        return render(request, self.template_name, context=context)


class ReportsView(LoginRequiredMixin, View):
    template_name = "console/admin/sessions.html"

    def get(self, request):
        appointments = Appointment.objects.all()
        context = {'appointments': appointments}
        return render(request, self.template_name, context=context)


class TransactionsView(LoginRequiredMixin, View):
    template_name = "console/admin/transactions.html"

    def get(self, request):
        transactions = BraintreeTransaction.objects.all()
        context = {'transactions': transactions}
        return render(request, self.template_name, context=context)
