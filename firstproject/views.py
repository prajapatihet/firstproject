from django.http import HttpResponse
from django.shortcuts import render

def homePage(req):
    data={
        'title': 'Home New Page',
        'bdata' : 'Welcome to Home Pages',
        'clist': ['PHP','Java','Django'],
        'student-details':[
            {'name':'het','phone':'9265504653'},
            {'name':'deep','phone':'9265154653'},
        ]
    }
    return render(req,"index.html",data)

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