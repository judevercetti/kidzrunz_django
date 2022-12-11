from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from console.forms import AppointmentForm

from website.models import Package

# Create your views here.


class Dashboard(LoginRequiredMixin, View):
    login_url = 'login'
    template_name = "dashboard.html"

    def get(self, request):
        template_name = f"console/admin/{self.template_name}" if request.user.is_staff else f"console/user/{self.template_name}"
        return render(request, template_name)


class MakeAppointment(LoginRequiredMixin, View):
    login_url = 'login'
    template_name = "console/user/make_appointment.html"

    def get(self, request):
        packages = Package.objects.all()
        context = {'packages': packages}
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = AppointmentForm(request.POST)
        print(dict(form.data.items()))
        if form.is_valid():
            print('valid')
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()

            return redirect("console:dashboard")
        else:
            print(form.errors)
            print('invalid')

class Sessions(View):
    template_name = "console/admin/sessions.html"

    def get(self, request):
        return render(request, self.template_name)
