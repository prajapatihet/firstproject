from django.http import HttpResponse

def aboutUs(req):
    return HttpResponse("<h1><b>Welcome to MyPage</b></h1>")
def courses(req):
    return HttpResponse("<h1><b>Welcome to CoursePage</b></h1>")

def courseDetails1(req,courseid):
    return HttpResponse(courseid)
def courseDetails2(req,courseid):
    return HttpResponse(courseid)
def courseDetails3(req,courseid):
    return HttpResponse(courseid)
def courseDetails4(req,courseid):
    return HttpResponse(courseid)