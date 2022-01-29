from django.shortcuts import render


# Create your views here.
def Home(request):
    return render(request, 'website/home.html')


def AboutUs(request):
    return render(request, 'website/about_us.html')