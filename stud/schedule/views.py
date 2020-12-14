from django.http import HttpResponse
from django.shortcuts import render

from .models import Class, Planned, Teaches
from course.models import Topic

# Create your views here.
def class_view(Request, batch_no='None', *args, **kargs):
    classes = []
    if batch_no == 'None':  
        pass
    else:
        for ind, c in enumerate(Class.objects.raw('SELECT * FROM class WHERE Class_no = ANY(SELECT Class_no FROM planned WHERE planned.Batch_no=%s) ORDER BY Class_Date, Start_Time;',[batch_no])):
            class_details = c
            print(type(c))
            classes.append({
                'course_name': Planned.objects.get(class_no=c.class_no).course.course_name,
                'date': class_details.class_date, 
                'start_time': class_details.start_time, 
                'end_time': class_details.end_time, 
                'imp_notice': class_details.imp_notice,
                'topics' : [Topic.objects.get(topic_no=t.topic_no_id, course=t.course_id).topic_name for t in Teaches.objects.filter(class_no=c.class_no)]
            })
    return render(Request, 'schedule.html', {'classes': classes})
