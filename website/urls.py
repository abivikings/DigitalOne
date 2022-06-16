from django.urls import path
from website.views import *
urlpatterns = [
    path('', Home, name='home'),
    path('about_us/', AboutUs, name='about_us'),
    path('contact_us/', ContactUs, name='contact_us'),
    path('app_suite/', AppSuite, name='app_suite'),
    path('esl/', ESL, name='esl'),
]
