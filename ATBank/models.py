from django.db import models

# Create your models here.
class login(models.Model):
    login_id=models.CharField(max_length=100,primary_key=True)
    password=models.CharField(max_length=100)
    email=models.EmailField()
    class Meta:
        db_table="login"
    def _str_(self):
        return self.login_id,self.password,self.email

class personal(models.Model):
    login_id=models.ForeignKey(login,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    address_Info=models.CharField(max_length=100)
    MobileNo=models.IntegerField(default=0)
    class Meta:
        db_table="personal"
    def _str_(self):
        return self.login_id,self.Name,self.address_info,self.MobileNo

class account(models.Model):
    login_id=models.ForeignKey(login,on_delete=models.CASCADE)
    locker_no=models.IntegerField(default=0)
    account_no=models.IntegerField(default=0)
    Type=models.CharField(max_length=100,default="savings")
    class Meta:
        db_table="account"
    def _str_(self):
        return self.login_id,self.locker_no,self.account_no

class otp_model(models.Model):
    otp=models.CharField(max_length=100)
    class Meta:
        db_table="otp_model"
    def _str_(self):
        return self.otp
