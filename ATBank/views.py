from django.shortcuts import render
from .forms import loginform, registerform, otp_form
from django.http import HttpResponseRedirect
from .models import login,personal,account,otp_model
from Crypto.Cipher import AES
from django.conf import settings
from django.core.urlresolvers import reverse
import pyotp
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import random
counter=0
key=b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'
cipher=AES.new(key)
# Create your views here.
def main(request):
    return render(request,'main.html')
def login_usr(request):
    form=loginform(request.POST)
    if request.method=='POST':        
       if form.is_valid():
          try:
             form1=form.clean_renewal_date()
             
             a1=login.objects.get(login_id=form1[0])
          except Exception:
             return render(request, 'login.html', {'form': form,'error_msg':"This id doesn't exit"})
          else:
             if form1[1]==a1.password:
                username=a1.login_id
                return HttpResponseRedirect(reverse('userpage',args=(username,)))
             else:
                return render(request, 'login.html', {'form': form,'error_msg':"wrong credetials"})
    else:     
       form1 = loginform()
       return render(request, 'login.html', {'form': form})
    
def register(request):
    if request.method=='POST':
       form=registerform(request.POST)
       if form.is_valid():
          form1=form.clean_renewal_date()
          acc=random.randint(1,10000000000)
          l_no=random.randint(1,1000)
          l1=login(login_id=form1[0],password=form1[1],email=form1[2])
          l1.save()
          p1=personal(Name=form1[5],address_Info=form1[3],MobileNo=form1[4],login_id=l1)
          p1.save()
          a1=account(account_no=acc,locker_no=l_no,Type=form1[6],login_id=l1)
          a1.save()
          return HttpResponseRedirect('thanks')
    else:
       form = registerform()
       return render(request, 'register.html', {'form': form})
   
def thanks(request):
    return render(request,'thanks.html')

def done(request):
    return render(request,'Done.html')

def about_us(request):
    return render(request,'about_us.html')

def branches(request):
    return render(request,'branches.html')

def contact(request):
    return render(request,'contact.html')

def userpage(request,username):
    a1=personal.objects.get(login_id=username)
    return render(request,'userpage.html',{'username':a1.Name})

def open_account(request):
    form=open_account(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
          
           form1=form.clean_renewal_date()
           acc=random.randint(1,10000000000)
           l_no=random.randint(1,1000)
           a1=account(account_no=acc,locker_no=l_no,Type=form1[1],login_id=l1)
           a1.save()
           p1=personal(Name=form1[0],address_Info=form1[2],MobileNo=form1[3],login_id=l1)
           p1.save()
           return HttpResponseRedirect(reverse('userpage',args=(username,)))
    else:
        form=open_account()
        return render(request,'open_account.html',{'form':form})

def open_locker(request,username):
    a1=personal.objects.get(Name=username)
    id=a1.login_id
    ac1=account.objects.get(login_id=id)
    return render(request,'open_locker.html',{'locker_no':ac1.locker_no,'username':username})

def view_details(request,username):
    a1=personal.objects.get(Name=username)
    return render(request,'details.html')

def otp(request,username):
    request.session.flush()
    form=otp_form(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form1=form.clean_renewal_date()
            a1=otp_model.objects.get(otp=form1[0])
            if a1.otp==form1[0]:
                return HttpResponseRedirect('done')
            else:
                return render(request,'otp.html',{'error_msg':"wrong otp"})
        
    else:
        a1=personal.objects.get(Name=username)
        id=a1.login_id
        l1=login.objects.get(login_id=id)
        email_id=l1.email
        pyotp.random_base32()
        totp = pyotp.TOTP('base32secret3232')
        num=totp.now()
        num1=str(num)
        o1=otp_model(otp=num1)
        o1.save()
        subject='your request otp'
        message=str(num)
        from_email=settings.EMAIL_HOST_USER
        to_email=[email_id]
        msg=EmailMessage(subject,message,from_email,to_email)
        msg.send()
        form=otp_form()
        return render(request,'otp.html',{'form':form})
    
