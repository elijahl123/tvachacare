from django.contrib import admin

from .models import PatientInformation, Account

# Register your models here.
admin.site.register(PatientInformation)
admin.site.register(Account)
