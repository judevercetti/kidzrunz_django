from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.utils.translation import gettext as _

# Create your views here.


class Dashboard(View):
    template_name = "console/dashboard.html"

    def get(self, request):
        return render(request, self.template_name)
