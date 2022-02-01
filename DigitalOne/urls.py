from django.urls import path, include
from .views import DashboardView
from django.contrib import admin

urlpatterns = [
    path('', include('website.urls')),
    path("", DashboardView.as_view(), name="dashboard"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("calender/", include("calendarapp.urls")),
]
