from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import login

class loginform(forms.Form):
     loginId=forms.CharField(label='loginId',max_length=100)
     password=forms.CharField(widget=forms.PasswordInput())
     class Meta:  
        model = login 
        fields = "__all__"  
     def clean_renewal_date(self):
        return self.cleaned_data['loginId'],self.cleaned_data['password']


class registerform(forms.Form):
     login_id=forms.CharField(label='login_id',max_length=100)
     password=forms.CharField(widget=forms.PasswordInput())
     email=forms.EmailField()
     address_Info=forms.CharField(max_length=100)
     MobileNo=forms.IntegerField(label='Mobile No')
     Name=forms.CharField(label='Name of account owner',max_length=100)
     Type=forms.CharField(label='Type of account',max_length=100)
     def clean_renewal_date(self):
        return self.cleaned_data['login_id'],self.cleaned_data['password'],self.cleaned_data['email'],self.cleaned_data['address_Info'],self.cleaned_data['MobileNo'],self.cleaned_data['Name'],self.cleaned_data['Type']

     

class otp_form(forms.Form):
     otp_no=forms.CharField(label='OTP')
     def clean_renewal_date(self):
          return self.cleaned_data['otp_no']


class open_account(forms.Form):
     Name=forms.CharField(label='Name of account owner',max_length=100)
     Type=forms.CharField(label='Type of account',max_length=100)
     address_Info=forms.CharField(max_length=100)
     MobileNo=forms.IntegerField(label='Mobile No')
     def clean_renewal_date(self):
        return self.cleaned_data['Name'],self.cleaned_data['Type'],self.cleaned_data['address_Info'],self.cleaned_data['MobileNo']
