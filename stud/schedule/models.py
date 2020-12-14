from django.db import models

from student.models import Batch
from course.models import Course, Topic

# Create your models here.


class Class(models.Model):
    # Field name made lowercase.
    class_no = models.IntegerField(db_column='Class_No', primary_key=True)
    # Field name made lowercase.
    class_date = models.DateField(
        db_column='Class_Date', blank=True, null=True)
    # Field name made lowercase.
    start_time = models.TimeField(
        db_column='Start_Time', blank=True, null=True)
    # Field name made lowercase.
    end_time = models.TimeField(db_column='End_time', blank=True, null=True)
    # Field name made lowercase.
    imp_notice = models.CharField(
        db_column='Imp_notice', max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class'


class Planned(models.Model):
    # Field name made lowercase.
    batch_no = models.OneToOneField(
        Batch, models.DO_NOTHING, db_column='Batch_no', primary_key=True)
    # Field name made lowercase.
    course = models.ForeignKey(
        Course, models.DO_NOTHING, db_column='Course_id')
    # Field name made lowercase.
    class_no = models.ForeignKey(
        Class, models.DO_NOTHING, db_column='Class_No')

    class Meta:
        managed = False
        db_table = 'planned'
        unique_together = (('batch_no', 'course', 'class_no'),)


class Teaches(models.Model):
    class_no = models.OneToOneField(
        Class, models.DO_NOTHING, db_column='class_no', primary_key=True)
    topic_no = models.ForeignKey(
        Topic, models.DO_NOTHING, db_column='topic_no', related_name='Topic_no')
    course = models.ForeignKey(Topic, models.DO_NOTHING, related_name='Course_id')

    class Meta:
        managed = False
        db_table = 'teaches'
        unique_together = (('class_no', 'topic_no', 'course'),)
