import braintree
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from console.forms import AppointmentForm
from console.models import Appointment, BraintreeCustomer, BraintreeTransaction

from website.models import Package

# Create your views here.


class Dashboard(LoginRequiredMixin, View):
    login_url = 'login'
    template_name = "console/user/dashboard.html"

    def get(self, request):
        appointments = Appointment.objects.filter(user=request.user).order_by('-created_on')
        context = {'appointments': appointments}
        return render(request, self.template_name, context=context)

    def post(self, request):
        appointment = Appointment.objects.get(pk=request.POST.get('appointment_id'))
        appointment.status = Appointment.Status.CANCELLED
        appointment.save()
        return redirect('console:dashboard')
        

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



class Sessions(View):
    template_name = "console/admin/sessions.html"

    def get(self, request):
        return render(request, self.template_name)


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
            success=True
        else:
            print("Transaction failed:")
            for error in result.errors.deep_errors:
                print(error.code, error.message)

        return JsonResponse({'success': success})
