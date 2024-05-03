from django.contrib import admin
from django.urls import path
from firstproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-us/',views.aboutUs),
    path('course/',views.courses),
]
