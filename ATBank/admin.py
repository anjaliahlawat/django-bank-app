from django.contrib import admin
from .models import login,personal,account,otp_model
# Register your models here.
admin.site.register(login)
admin.site.register(account)
admin.site.register(personal)
admin.site.register(otp_model)
