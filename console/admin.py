from django.contrib import admin

from console.models import Appointment, BraintreeCustomer, BraintreeTransaction

# Register your models here.


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'package', 'status', 'datetime')

@admin.register(BraintreeCustomer)
class BraintreeCustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'customer_id')

@admin.register(BraintreeTransaction)
class BraintreeTransactionAdmin(admin.ModelAdmin):
    list_display = ('customer', 'amount', 'transaction_id')
