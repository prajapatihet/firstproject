from django.contrib import admin
from django.urls import path
from firstproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-us/',views.aboutUs),
    path('course/',views.courses),
    path('courseStr/<str:courseid>',views.courseDetails1),
    path('courseInt/<int:courseid>',views.courseDetails2),
    path('courseSlug/<slug:courseid>',views.courseDetails3),
    path('courseAny/<courseid>',views.courseDetails4),
]
