from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth import login, authenticate, logout

from auth_app.models import User

# Create your views here.

class Login(View):
    template_name = "auth_app/login.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("console:dashboard")
        return render(request, self.template_name)

    def post(self, request):
        if not (request.POST.get("email") and request.POST.get("password")):
            messages.add_message(request, messages.ERROR,
                                 _("Please Fill all fields."))
            return redirect("auth_app:login")

        user = authenticate(
            username=request.POST.get("email"), password=request.POST.get("password")
        )
        if not user:
            messages.add_message(
                request, messages.ERROR, _("Account not found. Try Again.")
            )
            return redirect("login")

        login(request, user)
        if request.GET.get("next"):
            return redirect(request.GET.get("next"))
        return redirect("console:dashboard")


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("website:index")


class Signup(View):
    template_name = "auth_app/signup.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse("console:dashboard"))
        return render(request, self.template_name)

    def post(self, request):
        if not (
            request.POST.get("firstname")
            and request.POST.get("lastname")
            and request.POST.get("phone_number")
            and request.POST.get("email")
            and request.POST.get("password")
        ):
            print('Fill all fields')
            messages.add_message(request, messages.ERROR, _("Please Fill all fields."))
            return redirect(reverse("auth_app:signup"))

        if User.objects.filter(email=request.POST.get("email")):
            messages.add_message(request, messages.ERROR,
                                 _("Email not available."))
            return redirect("auth_app:signup")


        user = User.objects.create_user(
            first_name=request.POST.get("firstname"),
            last_name=request.POST.get("lastname"),
            phone_number=request.POST.get("phone_number"),
            email=request.POST.get("email"),
            username=f'{request.POST.get("firstname")}{request.POST.get("lastname")}'.lower(),
            password=request.POST.get("password"),
        )

        login(request, user)
        if request.GET.get("next"):
            return redirect(request.GET.get("next"))

        return redirect("console:dashboard")


class ForgotPassword(View):
    template_name = "auth_app/forgot_password.html"

    def get(self, request):
        return render(request, self.template_name)


class ResetPassword(View):
    template_name = "auth_app/reset_password.html"

    def get(self, request):
        return render(request, self.template_name)

