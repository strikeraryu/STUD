from django.db import models

# Create your models here.


class Batch(models.Model):
    # Field name made lowercase.
    stud_num = models.IntegerField(db_column='Stud_num', blank=True, null=True)
    # Field name made lowercase.
    batch_no = models.CharField(
        db_column='Batch_no', primary_key=True, max_length=4)

    class Meta:
        managed = False
        db_table = 'batch'


class Mentor(models.Model):
    # Field name made lowercase.
    mentor_id = models.IntegerField(db_column='Mentor_id', primary_key=True)
    # Field name made lowercase.
    mentor_name = models.CharField(
        db_column='Mentor_name', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    batch_no = models.ForeignKey(
        Batch, models.DO_NOTHING, db_column='Batch_no')

    class Meta:
        managed = False
        db_table = 'mentor'



