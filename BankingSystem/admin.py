from django.contrib import admin
from .models import Serviceuser, Deposit, Withdraw, SendMoney


# Register your models here.
admin.site.register(Serviceuser)
admin.site.register(Deposit)
admin.site.register(Withdraw)
admin.site.register(SendMoney)