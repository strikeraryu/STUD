from django.db import models

from student.models import Batch


class Course(models.Model):
    # Field name made lowercase.
    course_id = models.CharField(
        db_column='Course_id', primary_key=True, max_length=10)
    # Field name made lowercase.
    course_name = models.CharField(
        db_column='Course_name', max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class Enrolled(models.Model):
    # Field name made lowercase.
    batch_no = models.OneToOneField(
        Batch, models.DO_NOTHING, db_column='Batch_no', primary_key=True)
    # Field name made lowercase.
    course = models.ForeignKey(
        Course, models.DO_NOTHING, db_column='Course_id')
    # Field name made lowercase.
    teacher = models.CharField(
        db_column='Teacher', max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enrolled'
        unique_together = (('batch_no', 'course'),)


class Topic(models.Model):
    # Field name made lowercase.
    topic_no = models.IntegerField(db_column='Topic_no', primary_key=True)
    # Field name made lowercase.
    topic_name = models.CharField(db_column='Topic_name', max_length=255)
    # Field name made lowercase.
    module_no = models.IntegerField(
        db_column='Module_no', blank=True, null=True)
    # Field name made lowercase.
    weightage = models.FloatField(db_column='Weightage', blank=True, null=True)
    # Field name made lowercase.
    course = models.ForeignKey(
        Course, models.DO_NOTHING, db_column='Course_id')

    class Meta:
        managed = False
        db_table = 'topic'
        unique_together = (('topic_no', 'course'),)
