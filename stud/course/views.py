from django.http import HttpResponse
from django.shortcuts import render

from .models import Course, Enrolled

def course_view(Request, batch_no='None', *args, **kargs):
    courses = []
    if batch_no=='None':
        for c in Course.objects.all():
            print(c.course_name)
            courses.append(c.course_name)
    else:
        for e in Enrolled.objects.filter(batch_no=batch_no):
            course_name = Course.objects.get(course_id=e.course_id).course_name
            courses.append(course_name)
    return render(Request, 'course.html', {'courses' : courses})

def topic_view(Request, course_id='None', *args, **kargs):
    pass
