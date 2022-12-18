from django import forms

from console.models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        exclude = ('user', 'created_on', 'status')
