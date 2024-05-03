from django.http import HttpResponse

def aboutUs(req):
    return HttpResponse("<h1><b>Welcome to MyPage</b></h1>")
def courses(req):
    return HttpResponse("<h1><b>Welcome to CoursePage</b></h1>")