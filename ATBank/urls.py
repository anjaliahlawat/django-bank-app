from django.conf.urls import url

from ATBank import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^branches/$', views.branches, name='branches'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^login/$', views.login_usr, name='login_usr'),
    url(r'^register/$',views.register, name='register'),
    url(r'^register/thanks/$',views.thanks, name='thanks'),
    url(r'^login/userpage/(?P<username>\w+)/$', views.userpage, name='userpage'),
    url(r'^login/userpage/(?P<username>\w+)/open_locker/$', views.open_locker, name='open_locker'),
    url(r'^login/userpage/(?P<username>\w+)/details/$', views.view_details, name='details'),
    url(r'^login/userpage/(?P<username>\w+)/open_locker/otp/$', views.otp, name='otp'),
    url(r'^login/userpage/(?P<username>\w+)/open_locker/otp/done/$', views.done, name='done'),
    url(r'^login/userpage/open_account/$', views.open_account, name='open_account'),
]
