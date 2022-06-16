from django.shortcuts import render


# Create your views here.
def Home(request):
    return render(request, 'website/home.html')


def AboutUs(request):
    return render(request, 'website/about_us.html')


def ContactUs(request):
    return render(request, 'website/contact_us.html')


def AppSuite(request):
    return render(request, 'website/app_suite.html')


def ESL(request):
    return render(request, 'website/esl.html')