from django.db import models

from student.models import Batch


class Course(models.Model):
    course_id = models.CharField(db_column='Course_id', primary_key=True, max_length=10)  # Field name made lowercase.
    course_name = models.CharField(db_column='Course_name', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'course'

class Enrolled(models.Model):
    batch_no = models.OneToOneField(Batch, models.DO_NOTHING, db_column='Batch_no', primary_key=True)  # Field name made lowercase.
    course = models.ForeignKey(Course, models.DO_NOTHING, db_column='Course_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'enrolled'
        unique_together = (('batch_no', 'course'),)