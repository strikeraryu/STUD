from django.http import HttpResponse
from django.shortcuts import render

from .models import Course, Enrolled, Topic
from schedule.models import Class, Teaches, Planned


def course_view(Request, batch_no='None', *args, **kargs):
    courses = []
    total_course = 0
    if batch_no == 'None':
        for ind, c in enumerate(Course.objects.all()):
            total_course += 1
            courses.append(
                {"id": ind+1, "course_name": c.course_name, "course_id": c.course_id})
    else:
        for ind, e in enumerate(Enrolled.objects.filter(batch_no=batch_no)):
            total_course += 1
            course_name = Course.objects.get(course_id=e.course_id).course_name
            courses.append(
                {"id": ind+1, "course_name": course_name, "course_id": e.course_id, 'teacher': e.teacher})
    return render(Request, 'course.html', {'courses': courses, "total_course": total_course, 'batch_no': batch_no})


def topic_view(Request, course_id='None', *args, **kargs):
    topics = []

    if course_id == 'None':
        for ind, c in enumerate(Course.objects.all()):
            total_course += 1
            courses.append(
                {"id": ind+1, "course_name": c.course_name, "course_id": c.course_id})
    else:
        for ind, t in enumerate(Topic.objects.raw('select * from Topic where Course_id = %s ', [course_id])):
            topics.append({
                'id': ind+1,
                'topic_name': t.topic_name,
                'weightage': t.weightage,
                'module_no': t.module_no,
                'classes': [
                    {
                        'id': i+1,
                        'batch_no': Planned.objects.get(class_no = c.class_no).batch_no.batch_no,
                        'date': c.class_date,
                        'start_time': c.start_time,
                        'end_time': c.end_time
                    }
                    for i, c in enumerate(Class.objects.raw('SELECT * FROM Class WHERE class_no = ANY(SELECT class_no FROM Teaches WHERE Teaches.topic_no = %s and Teaches.Course_id = %s);', [t.topic_no, t.course.course_id]))
                ],
                'tot_classes': len(Class.objects.raw('SELECT * FROM Class WHERE class_no = ANY(SELECT class_no FROM Teaches WHERE Teaches.topic_no = %s and Teaches.Course_id = %s);', [t.topic_no, t.course.course_id]))
            })
        return render(Request, 'topic.html', {'topics': topics})
